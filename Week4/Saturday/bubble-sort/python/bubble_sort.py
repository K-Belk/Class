sequence = [4, 3, 5, 0, 1]


def bubble_sort(seq):
    idx = 1
    swaps = 0
    while idx < len(seq):
        previous = seq[idx - 1]
        current = seq[idx]
        if previous > current:
            hold = previous
            seq[idx], seq[idx - 1] = hold, current
            idx = 1
            swaps += 1
        else:
            idx += 1
    print(f"Final result: {seq}")
    print(f"Swaps: {swaps}")
    return seq


print(bubble_sort(sequence))


