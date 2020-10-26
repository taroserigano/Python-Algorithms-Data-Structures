def binary_search(sequence, item):
  begin_index = 0
  end_index = len(sequence) - 1

  while begin_index <= end_index:
    midpoint = begin_index + (end_index - begin_index) // 2
    midpoint_value = sequence[midpoint]
    if midpoint_value == item:
      return midpoint

    elif item < midpoint_value:
      end_index = midpoint - 1  

    else:
      begin_index = midpoint + 1

  return None

sequence1 = [2,4,5,6,8,9,12,34]
item_a = 12

print(binary_search(sequence1, item_a))

print(binary_search(sequence1, 109))