def sum_pairs(array, pair):
    results = []
    for i in array:
        for j in range(i, len(array)):
            if (i + array[j] == pair):
                results = results + [[i,array[j]]]
    if len(results) > 0:
        return results
    return 'unable to find pairs'