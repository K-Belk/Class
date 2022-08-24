def linear_search(value_to_find, array_to_search_through):
    for i in range(len(array_to_search_through)) :
        if value_to_find == array_to_search_through[i]:
            return i


def linear_search_global(value_to_find, array_to_search_through):
    result = []
    for i in range(len(array_to_search_through)) :
        if value_to_find == array_to_search_through[i]:
            result.append(i)
    if len(result) > 0:
        return result

