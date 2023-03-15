# Prompt user for directory path
read -p "Enter the directory path: " dir_path

# Check if directory exists
if [ ! -d "$dir_path" ]; then
    echo "The directory path entered does not exist."
    exit 1
fi

# Prompt user for regular expression pattern
while true; do
    read -p "Enter a regular expression pattern to match the file names: " pattern
    if ! grep -qP "$pattern" <<< ""; then
        break
    else
        echo "The regular expression pattern entered is not valid. Please try again."
    fi
done

# Create function to be called when file changes are detected
process_file() {
    # Backup file to separate directory
    backup_dir="backup"
    if [ -d "$backup_dir" ]; then
        read -p "A backup directory already exists. Do you want to overwrite it? (y/n): " overwrite
        if [ "$overwrite" = "y" ]; then
            rm -rf "$backup_dir"
            mkdir "$backup_dir"
        else
            i=2
            while [ -d "${backup_dir}_$i" ]; do
                ((i++))
            done
            backup_dir="${backup_dir}_$i"
            mkdir "$backup_dir"
        fi
    else
        mkdir "$backup_dir"
    fi
    cp "$1" "$backup_dir"

    # Modify file contents
    if grep -q "specific string" "$1"; then
        awk '/specific string/ { print $1,$2,$3 }' "$1" > "$1.tmp"
        sed 's/specific string/new value/g' "$1" > "$1.tmp"
        mv "$1.tmp" "$1"
    fi

    # Extract first and last 5 lines if file is more than 10 lines long
    if [ $(wc -l < "$1") -gt 10 ]; then
        head -n 5 "$1" > "$1.head"
        tail -n 5 "$1" > "$1.tail"
    fi

    # Compress backup directory with timestamp in filename
    timestamp=$(date +%Y%m%d%H%M%S)
    tar -czf "${backup_dir}_${timestamp}.tar.gz" "$backup_dir"
    rm -rf "$backup_dir"
}

# Monitor directory for changes to files matching regular expression pattern
while true; do
    inotifywait -e modify,create,delete "$dir_path" | grep -E "$pattern" | while read file; do
        process_file "$file"
    done
done

# If no files match pattern, print message and exit
if [ $(find "$dir_path" -type f -name "$pattern" | wc -l) -eq 0 ]; then
    echo "There are no files in the specified directory or its subdirectories that match the specified regular expression pattern."
    exit 1
fi

# If there is an error, print message and exit
if [ "$?" -ne 0 ]; then
    echo "An error occurred. Exiting script."
    exit 1
fi
