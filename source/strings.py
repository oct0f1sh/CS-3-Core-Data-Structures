#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if text == '':
        return False
    elif pattern == '':
        return True

    if text[0] == pattern[0]:
        if len(pattern) == 1:
            return True
        for i in range(1, len(pattern)):
            if len(text) < len(pattern):
                return False

            if text[i] == pattern[i] and i == len(pattern) - 1:
                return True
            elif text[i] == pattern[i]:
                continue
            else:
                text = text[i:]
                return contains(text, pattern)
    else:
        text = text[1:]
        return contains(text, pattern)
    # TODO: Implement contains here (iteratively and/or recursively)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    iterator = 0
    index = 0

    for char in text:
        if char == pattern[iterator]:
            if char == pattern[iterator] and iterator == len(pattern) - 1:
                print('nice')
                return index - iterator
            iterator += 1
        else:
            iterator = 0
        index += 1


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # # TODO: Uncomment these lines after you implement find_all_indexes
    # indexes = find_all_indexes(text, pattern)
    # print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
