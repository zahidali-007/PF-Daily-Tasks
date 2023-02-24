def create_multi_array(n, m):
    arr = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        row = "|"
        for j in range(m):
            arr[i][j] = f"{i+1},{j+1}"
            row += f" {arr[i][j]} |"
        print(row)
        if i == 0:
            print("-" * len(row))

create_multi_array(3, 4)
