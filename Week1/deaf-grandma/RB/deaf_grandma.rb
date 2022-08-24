def deaf_grandma()
  bye_count = 0

  while true
    puts 'Kid: '
    input_text = gets.chomp
    if input_text == ''
      puts 'Grandma:'    
      puts 'WHAT?'
    elsif input_text != input_text.upcase
      puts 'Grandma:'    
      puts 'SPEAK UP, KID!'    
    elsif input_text == 'GOODBYE!'
      bye_count += 1
      if bye_count <= 1
        puts 'Grandma:'    
        puts 'LEAVING SO SOON?'
      elsif bye_count >= 2
        puts 'Grandma:'
        puts 'LATER SKATER'
        break
      end
    elsif input_text == input_text.upcase
      puts 'Grandma:'
      puts 'NO, NOT SINCE 1946!'
    end
  end
end

deaf_grandma()