require './anagram2.rb'

list_of_words = ["threads", "trashed", "hardest", "hatreds", "hounds"]

puts(anagram_for("threads", list_of_words) == ["threads", "trashed", "hardest", "hatreds"])
puts(anagram_for("apple", list_of_words) == [])