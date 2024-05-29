def find_pair(nums, target):
    idx_map = {}
    for i, num in enumerate(nums):
        required_num = target - num
        if required_num in idx_map:
            return [i, idx_map[required_num]]
        else:
            print(f"Adding to hash table: key:{num}, value: {i}")  # print statement added
            idx_map[num] = i
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
