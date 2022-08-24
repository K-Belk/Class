require "./roman_numerals.rb"

puts(toRomansLazy(1) == 'I')
puts(toRomansLazy(3) == 'III')
puts(toRomansLazy(4) == 'IIII')

puts(toRomansModern(4) == 'IV')
puts(toRomansModern(944) == 'CMXLIV')
puts(toRomansModern(150) == 'CL')