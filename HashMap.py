def find_pair(nums, target):
    # Initialize an empty dictionary to store the numbers in the array as keys and their indices as values
    idx_map = {}

    # Iterate over the array with both index and value
    for i, num in enumerate(nums):
        # Calculate the number required to reach the target by subtracting the current number from the target
        required_num = target - num

        # If the required number is already in the dictionary, that means we have found a pair that adds up to the target
        if required_num in idx_map:
            # Return the indices of the pair in the order they were encountered in the array
            return [i, idx_map[required_num]]
        else:
            # If the required number is not in the dictionary, add the current number and its index to the dictionary
            print(f"Adding to hash table: key:{num}, value: {i}")  # print statement added
            idx_map[num] = i

    # If no pair is found that adds up to the target, return None
    return None


print("Test 1:")
nums = [1, 2, 3]
target = 4
print(find_pair(nums, target))  # Output: [2, 0]
print("\n")
print("Test 2:")
nums = [7, 2, 13, 11, 8]
target = 24
print(find_pair(nums, target))  # Output: [3, 2]
print("\n")
print("Test 3:")
nums = [2, 1, 7, 11, 15, 17]
target = 18
print(find_pair(nums, target))  # Output: [3, 2]
