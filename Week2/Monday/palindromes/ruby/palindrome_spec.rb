require './palindrome.rb'
puts(palindrome('racecar') == true)
puts(palindrome('Noon') == true)
puts(palindrome('ciVic') == true)
puts(palindrome('nice') == false)
puts(palindrome(434) == true)
puts(palindrome(123) == false)
puts(palindrome('bomb') == false)

puts("The following should be true if you're trying to do the extra portion of this challenge")
puts(palindrome('Sore was I ere I saw Eros.') == true)
puts(palindrome('A man, a plan, a canal -- Panama') == true)