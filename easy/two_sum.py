"""
Two Sum - Easy
LeetCode #1

Given an array of integers nums and an integer target,
return the indices of the two numbers that add up to target.

Approach: Brute Force (nested loops)
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Check every combination of two numbers
        for i in range(len(nums)):
            for j in range(len(nums)):
                # Make sure we're not using the same element twice
                if i != j and nums[i] + nums[j] == target:
                    return [i, j]


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(sol.twoSum([3, 2, 4], 6))       # [1, 2]
    print(sol.twoSum([3, 3], 6))          # [0, 1]