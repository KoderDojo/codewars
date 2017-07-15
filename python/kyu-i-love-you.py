words = ['I love you', 'a little', 'a lot',
         'passionately', 'madly', 'not at all']


def how_much_i_love_you(nb_petals):
    """
    Returns the word associated with nb_petals.
    
    :param nb_petals: int, petal number.
    :return: str, the word associated with the petal number.
    
    >>> assert(how_much_i_love_you(7) == 'I love you')
    >>> assert(how_much_i_love_you(3) == "a lot")
    >>> assert(how_much_i_love_you(6) == "not at all")
    """
    return words[(nb_petals - 1) % len(words)]
