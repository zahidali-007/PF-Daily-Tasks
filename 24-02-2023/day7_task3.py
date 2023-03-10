import random

def add_to_list(value, lst):
    if value in lst:
        print(f"Value '{value}' already exists in the list.")
    else:
        lst.append(value)
        print(f"Added '{value}' to the list.")
        index = lst.index(value)
        sublist = lst[:index+1]
        print(f"List up until '{value}': {sublist}")

my_list = [random.randint(0, 10) for _ in range(10)]
print(f"Initial list: {my_list}")
add_to_list(2, my_list)  # Value '2' already exists in the list
add_to_list(7, my_list)  # Added '7' to the list. List up until '7': [6, 2, 1, 0, 6, 2, 7]
