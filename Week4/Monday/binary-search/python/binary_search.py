
import math
import random

values = random.sample(list(range(1,10000)), 1000)
values.sort()

def find_middle(range_min, range_max):
    return math.floor((range_min + range_max)/2)

def binary_search(num, lst_nums, search_min=0, search_max=0):
    if search_min == 0:
        search_min = lst_nums[0]
    if search_max == 0:
        search_max = lst_nums[len(lst_nums)-1] +1
    mid = find_middle(search_min, search_max)
    
    if num not in lst_nums:
        return -1
    elif num > mid:
        return binary_search(num, lst_nums, mid, search_max)
    elif num < mid:
        return binary_search(num, lst_nums, search_min, mid)
    elif num == mid:
        return lst_nums.index(num)


