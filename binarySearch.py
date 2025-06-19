#!/usr/bin/python3

"""
Binary search algorithm
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

def test_binary_search():
    solution = Solution()

    # Test case 1: Target found in the middle of array
    nums = [1, 3, 5, 7, 9]
    target = 5
    result = solution.search(nums, target)
    if result != -1:
        print(f"SUCCESS: Found target {target} at index {result}")
    else:
        print(f"FAIL: Target {target} not found, in the array")

    # Test case 2: Target not found
    nums = [1, 3, 5, 7, 9]
    target = 4
    result = solution.search(nums, target)
    if result != -1:
        print(f"SUCCESS: Found target {target} at index {result}")
    else:
        print(f"FAIL: Target {target} not found, in the array")

    # Test case 3: Edge case - empty array
    nums = []
    target = 5
    result = solution.search(nums, target)
    if result != -1:
        print(f"SUCCESS: Found target {target} at index {result}")
    else:
        print(f"FAIL: Target {target} not found, in the array")

if __name__ == "__main__":
    test_binary_search()
                         
