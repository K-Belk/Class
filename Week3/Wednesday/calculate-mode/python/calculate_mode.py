from typing import Counter


def calculate_mode(list_in):
    counted = {}
    for value in list_in:
        if value in counted:
            counted[value] += 1
        else:
            counted[value] = 1
    sorted_count = Counter(counted)
    results = []
    greatest = 0
    for m in sorted_count.most_common():
        if m[1] >= greatest:
            results.append(m[0])
            greatest = m[1]
        else:
            return results
        
    return results

