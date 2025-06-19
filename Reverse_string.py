#!/usr/bin/python3

import unittest
from typing import List

"""Write a function that reverses a string. The input string is given as an array of characters
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left +=1
            right -=1

class TestReverseString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_string(self):
        """Test reversing an empty list"""
        s = []
        self.solution.reverseString(s)
        self.assertEqual(s, [])

    def test_single_character(self):
        """Test reversing a list with a single character"""
        s = ["a"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["a"])

    def test_even_length_string(self):
        """Test reversing a list with even number of characters"""
        s = ["h", "e", "l", "l", "o"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_odd_length_string(self):
        """Test reversing a list with odd number of characters"""
        s = ["H", "a", "n", "n", "a", "h"]
        self.solution.reverseString(s)
        self.assertEqual(s, ["h", "a", "n", "n", "a", "H"])

    def test_with_special_characters(self):
        """Test reversing a list with special characters"""
        s = ["!", "@", "#", "$", "%"]
        expected = ["%" ,"$", "#", "@", "!"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_with_mixed_characters(self):
        """Test reversing a list with mixed alphanumeric and special characters"""
        s = ["a", "1", "b", "2", "!"]
        expected = ["!", "2", "b", "1", "a"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_with_duplicate_characters(self):
        """Test reversing a list with duplicate characters"""
        s = ["a", "a", "b", "b", "c"]
        expected = ["c", "b", "b", "a", "a"]
        self.solution.reverseString(s)
        self.assertEqual(s, expected)

    def test_palindrome(self):
        """Test reversing a palindrome (should remain the same)"""
        original = ["r", "a", "c", "e", "c", "a", "r"]
        s = original.copy()  # Make a copy to avoid modifying the original
        self.solution.reverseString(s)
        # The reversed palindrome should be equal to the original
        self.assertEqual(s, original)
        # But we want to make sure it's actually reversed, not just unchanged
        self.assertEqual(s, ["r", "a", "c", "e", "c", "a", "r"])

    def test_large_input(self):
        """Test with a large input list"""
        # Create a list with 10,000 characters
        large_list = [str(i % 10) for i in range(10000)]
        # Expected result is the reverse of the original list
        expected = large_list.copy()
        expected.reverse()

        self.solution.reverseString(large_list)
        self.assertEqual(large_list, expected)

    def test_in_place_modification(self):
        """Test that the function modifies the list in-place"""
        s = ["h", "e", "l", "l", "o"]
        id_before = id(s)
        self.solution.reverseString(s)
        id_after = id(s)
        # The id should remain the same, indicating in-place modification
        self.assertEqual(id_before, id_after)
        # The content should be reversed
        self.assertEqual(s, ["o", "l", "l", "e", "h"])

    def test_multiple_reversals(self):
        """Test that reversing a string twice returns the original string"""
        original = ["P", "y", "t", "h", "o", "n"]
        s = original.copy()

        # First reversal
        self.solution.reverseString(s)
        self.assertEqual(s, ["n", "o", "h", "t", "y", "P"])

        # Second reversal should return to original
        self.solution.reverseString(s)
        self.assertEqual(s, original)


if __name__ == "__main__":
    unittest.main()
                                                                  
