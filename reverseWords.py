#!/usr/bin/python3

def reverse_words(s):
    """
    Reverse the order of words in a string.

    Args:
        s (str): Input string with words separated by spaces

    Returns: 
        str: String with words in reverse order, single space separated
    """
    # Method 1: Using split() and reverse
    # split() with no argument splits on any whitespace and remove empty strings
    words = s.split()

    # Reverse the list of words
    words.reverse()

    # Join with single spaces
    return ' '.join(words)

def reverse_words_oneliner(s):
    """
    One-liner version using slicing
    """
    return ' '.join(s.split()[::-1])

def reverse_words_manual(s):
    """
    Manual implementation without using built-in reverse
    """
    words = s.split()
    result = []

    # Add words in reverse order
    for i in range(len(words) - 1, -1, -1):
        results.append(words[i])

    return ' '.join(result)

# Test cases
def test_reverse_words():
    test_cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world  ", "world hello"),
        ("a good   example", "example good a"),
        ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
        ("Alice", "Alice"),
        ("", ""),
        ("   ", "")
    ]

    print("Testing reverse_words function:")
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = reverse_words(input_str)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {status}")
        print(f"  Input: '{input_str}'")
        print(f"  Expected: '{expected}'")
        print(f"  Got: '{result}'")
        print()


if __name__ == "__main__":
    test_reverse_words()
