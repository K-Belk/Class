from linear_search import linear_search
from linear_search import linear_search_global

print(linear_search(3, [1,2,3]) == 2)
print(linear_search(4, [1,2,3]) == None)
print(linear_search(13, [1,2,3]) == None)

print(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5])
print(linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6])
print(linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4])
