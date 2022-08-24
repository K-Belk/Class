def linear_search(value_to_find, array_to_search_through)
  for i in 0...array_to_search_through.length() do
    if value_to_find == array_to_search_through[i]
      return i
    end
  end
  return
end

def linear_search_global(value_to_find, array_to_search_through)
  result = []
  for i in 0...array_to_search_through.length() do
    if value_to_find == array_to_search_through[i]
      result.append(i)
    end
  end
  if result.length() > 0
    return result
  end
end