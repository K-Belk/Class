

from re import T


def flatten_list(lst):

    if not isinstance(lst, list):
        return 'not a list'

    elif len(lst) == 0:
        return lst

    elif isinstance(lst[0], list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])

    else:
        return lst[:1] + flatten_list(lst[1:])

raise TypeError