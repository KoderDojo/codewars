"""
For a given string s find the character c with longest
consecutive repetition and return a tuple (c, l)
(in Haskell Just (Char, Int), in C# Tuple<char?, int>)
where l is the length of the repetition. If there are
two or more characters with the same l return the first.

For empty string return ('', 0) (in Haskell Nothing,
in C# Tuple<char, int>(null, 0)).

Happy coding! :)
"""


def longest_repetition(chars):
    """
    >>> assert(longest_repetition(None) == ('', 0))
    >>> assert(longest_repetition('') == ('', 0))
    >>> assert(longest_repetition('a') == ('a', 1))
    >>> assert(longest_repetition('ab') == ('a', 1))
    >>> assert(longest_repetition('aaaaaabbbbbcccc') == ('a', 6))
    >>> assert(longest_repetition('aaaabbbbbbccccc') == ('b', 6))
    >>> assert(longest_repetition('aaaabbbbbcccccc') == ('c', 6))
    """
    if chars is None or len(chars) == 0:
        return '', 0

    chars_length = len(chars)

    if chars_length == 1:
        return chars, 1

    longest_repeating_char, longest_repeating_count = '', 0
    previous_char, current_count = '', 0

    for i, char in enumerate(chars):
        if char == previous_char:
            current_count += 1
            if i != chars_length - 1:
                continue

        if current_count > longest_repeating_count:
            longest_repeating_count = current_count
            longest_repeating_char = previous_char

        current_count = 1
        previous_char = char

    return longest_repeating_char, longest_repeating_count
