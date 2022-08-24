def bottle_song(count)
	for i in (count).downto(1)
    puts "#{i} bottles of beer on the wall, #{i} bottles of beer.
    Take one down and pass it around, #{i - 1} bottles of beer on the wall."
  end
  puts "No more bottles of beer on the wall, no more bottles of beer.
  Go to the store and buy some more, 99 bottles of beer on the wall."
end

bottle_song(10)