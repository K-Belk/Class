def pad(array, min_size, value = None):
    """
    Pad will accept a list, a minimum size (non-negative integer) for the list, and an optional argument of what the list should be "padded" with.

    If the list is longer than what the minimun size is, then continue to add the padded value to the end till the minimum size of the list is reached

    If the list's length is less than the minimum size, `pad` should return a new list padded with the pad value up to the minimum size.

    >>>> pad([1,2,3], 5)

    returns >>> [1,2,3,None,None]

    """
    results = array
    if len(array) < min_size:
        size_difference = min_size - len(array)
        for i in range(size_difference):
            results.append(value)
    return results