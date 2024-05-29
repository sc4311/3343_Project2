def find_pair(nums, target):
    # Get the length of the list
    n = len(nums)

    # Iterate over the list, excluding the last element
    for i in range(n - 1):
        # Iterate over the remaining elements in the list
        for j in range(i + 1, n):
            # If the sum of the current pair equals the target
            if nums[i] + nums[j] == target:
                # Return the indices of the pair
                return [i, j]
    # If no pair is found that sums to the target, return None
    return None


print("Test 1: ")
nums = [1, 2, 3]
target = 4
print(find_pair(nums, target))  # Output: [0, 2]
print("\n")
print("Test 2: ")
nums = [7, 2, 13, 11]
target = 24
print(find_pair(nums, target))  # Output: [2, 3]
print("\n")
print("Test 3: ")
nums = [2, 1, 7, 11, 15, 17]
target = 18
print(find_pair(nums, target))  # Output: [1, 5]

