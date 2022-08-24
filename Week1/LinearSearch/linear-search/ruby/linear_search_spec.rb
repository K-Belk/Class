require './linear_search.rb'

puts(linear_search(3, [1,2,3]) == 2)
puts(linear_search(4, [1,2,3]) == nil)
puts(linear_search(13, [1,2,3]) == nil)

puts(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]) == [1, 3, 5])
puts(linear_search_global("s", ["b", "a", "n", "a", "n", "a", "s"]) == [6])
puts(linear_search_global("n", ["b", "a", "n", "a", "n", "a", "s"]) == [2, 4])
