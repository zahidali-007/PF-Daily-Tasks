def add_to_list(value, lst):
    if len(lst) >= 5:
        lst.pop()
    lst.insert(0, value)
    print(f"Added '{value}' to the list.")


my_list = []
add_to_list(1, my_list)  # Added '1' to the list.
add_to_list(2, my_list)  # Added '2' to the list.
add_to_list(3, my_list)  # Added '3' to the list.
add_to_list(4, my_list)  # Added '4' to the list.
add_to_list(5, my_list)  # Added '5' to the list.
add_to_list(6, my_list)  # Added '6' to the list. Removed '1' from the list.