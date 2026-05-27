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
        seen = {}
        for i in range(len(nums)):
            needed = target - nums[i]
            
            if needed in seen:
                return [seen[needed], i]
            
            seen[nums[i]] = i