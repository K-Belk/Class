ConversionTableLazy = [
  {decimal: 1000, roman: 'M'},
  {decimal: 500, roman: 'D'},
  {decimal: 100, roman: 'C'},
  {decimal: 50, roman: 'L'},
  {decimal: 10, roman: 'X'},
  {decimal: 5, roman: 'V'},
  {decimal: 1, roman: 'I'},
]

def toRomansLazy (num)
  roman_num_result = ""

  for i in 0...ConversionTableLazy.length() do
    
    disvisible_by = (num / ConversionTableLazy[i][:decimal]).floor

    num = num % ConversionTableLazy[i][:decimal]

    j = 0

    while j < disvisible_by do
      roman_num_result += ConversionTableLazy[i][:roman]
      j += 1
    end
  end
  return roman_num_result
end

ConversionTableModern = [
  {decimal: 1000, roman: 'M'},
  {decimal: 900, roman: 'CM'},
  {decimal: 500, roman: 'D'},
  {decimal: 400, roman: 'CD'},
  {decimal: 100, roman: 'C'},
  {decimal: 90, roman: 'XC'},
  {decimal: 50, roman: 'L'},
  {decimal: 40, roman: 'XL'},
  {decimal: 10, roman: 'X'},
  {decimal: 9, roman: 'IX'},
  {decimal: 5, roman: 'V'},
  {decimal: 4, roman: 'IV'},
  {decimal: 1, roman: 'I'}    
]

def toRomansModern(num)
  roman_num_result = ""

  for i in 0...ConversionTableModern.length() do
    disvisible_by = (num / ConversionTableModern[i][:decimal]).floor

    num = num % ConversionTableModern[i][:decimal]

    j = 0

    while j < disvisible_by do
      roman_num_result += ConversionTableModern[i][:roman]
      j += 1
    end
  end
  return roman_num_result
end