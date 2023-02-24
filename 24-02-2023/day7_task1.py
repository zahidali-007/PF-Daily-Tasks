def add_to_list(key, value, lst):
    if key in lst:
        print(f"Key '{key}' already exists. Please choose another key.")
    elif len(lst) >= 10:
        print("List is full. Cannot add more items.")
    else:
        lst.append((key, value))
        print(f"Added '{value}' with key '{key}' to the list.")

my_list = []
add_to_list("apple", 1, my_list)  # Added '1' with key 'apple' to the list.
add_to_list("banana", 2, my_list)  # Added '2' with key 'banana' to the list.
add_to_list("apple", 3, my_list)  # Key 'apple' already exists. Please choose another key.
add_to_list("cherry", 4, my_list)  # Added '4' with key 'cherry' to the list.