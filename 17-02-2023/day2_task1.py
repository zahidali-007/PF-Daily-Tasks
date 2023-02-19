def add_sorted_num(nums, num):
    # Sort the list of numbers
    nums.sort()
    # Find the index where the number should be added
    index = 0
    while index < len(nums) and nums[index] < num:
        index += 1
    # Insert the number at the appropriate position
    nums.insert(index, num)
    return nums

# Example usage
input_list = input("Enter a list of integers separated by spaces: ").split()
nums = [int(num) for num in input_list]
print("Original list:", nums)

new_num = int(input("Enter a new integer to add to the list: "))
nums = add_sorted_num(nums, new_num)

print("Sorted list with new number added:", nums)
