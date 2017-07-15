def first_non_repeating_letter(the_string):
    """
    Find first non-repeating letter in a string.
    Letters are to be treated case-insensitive,
    which means 't' = 'T'. However, one must
    return the first non-repeating letter as it
    appears in the string, either in uppercase
    or lowercase.

    'sTress' -> 'T'

    :param the_string: str, letters of alphabet
    :return: str, single letter or ''
    """
    single_letters = {}

    # if the left index and right index of the letter
    # are the same, we have a single letter. Here we
    # enumerate on the lowercase version of the string
    # so uppercase and lowercase letters are treated
    # identically.
    lowercase_string = the_string.lower()
    for index, letter in enumerate(lowercase_string):
        if lowercase_string.find(letter) == lowercase_string.rfind(letter):
            single_letters[letter] = index

    if len(single_letters) == 0:
        return ''

    # pick single letter with smallest index
    lowercase_first_letter, index =\
        min(single_letters.items(), key=lambda l: l[1])

    # display the letter from the original string
    # because it could be uppercase
    return the_string[index]


print(first_non_repeating_letter('lkKULg;gH2SI3zm2P8aI5YjB5;b4hsG26.xnuS'))

