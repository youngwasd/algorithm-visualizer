# Given an array of integers nums and an integer target, 
# return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j
# that satisfy the condition.

# Return the answer with the smaller index first. 

# ex 1
# input: nums = [3, 4, 5, 6], target = 7
# output: [0, 1]
# explanation: nums[0] + nums[1] == 7, so we return [0, 1]

# hashing
# brute force solution
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # brute force

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i,j] #if this doesnt return ture
        return [0, 0]


sol = Solution()
result = sol.twoSum([3, 4, 5, 6], 7)
expected = [0, 1]

correct = "fail"
if result == expected:
    correct = 'pass'

print(correct)
print(result)
print(expected)


# java pseudo brute force solution first then write in python
# int[] twoSum(int[] arr, target)
# for i = 0 to arr length
# for j = i + 1 to arr length
# if target == arr[i] + arr[j]
# return [i, j]
# break as we return only one pair
# else print(young sucks)



#Solution
# int[] twoSum(int[] arr, target)
# map<key, value> Map = HashMap<>
# for i = 0 < arr.length: i++
# temp = target - arr[i]

