VOWELS = 'aeiouy'
TRIPLE_SCORES = {}


def word_groups(word):
    """
    >>> list(word_groups('weight'))
    ['w', 'ei', 'ght']
    >>> list(word_groups('eightyfive'))
    ['ei', 'ght', 'y', 'f', 'i', 'v', 'e']
    """
    index = 0
    while index < len(word):
        # Find some consonants.
        start = index
        while index < len(word) and word[index] not in VOWELS:
            index += 1
        if index > start:
            yield word[start:index]
        # Find some vowels.
        start = index
        while index < len(word) and word[index] in VOWELS:
            index += 1
        if index > start:
            yield word[start:index]


def word_triples(word):
    """
    >>> list(word_triples('weight'))
    ['^wei', 'weight', 'eight$']
    >>> list(word_triples('eightyfive'))
    ['^eight', 'eighty', 'ghtyf', 'yfi', 'fiv', 'ive', 've$']
    """
    groups = ['^'] + list(word_groups(word)) + ['$']
    for start in range(len(groups) - 2):
        yield ''.join(groups[start:start + 3])


def readability(word):
    """
    >>> readability('xxyhcwx')
    0
    >>> readability('shlomo')
    625
    >>> readability('shoebox')
    700
    >>> readability('merchandise')
    1337
    >>> readability('antidisestablishmentarianism')
    1515
    >>> readability('are')
    1900
    >>> readability('interesting')
    1962
    """
    result = 0
    triples = list(word_triples(word))
    for triple in triples:
        result += TRIPLE_SCORES.get(triple, 0)
    return result * 100 / len(triples)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
