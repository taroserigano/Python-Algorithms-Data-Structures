def quick_sort(list):
  length = len(list)
  if length <= 1:
    return list
  else: 
    pivot = list.pop()

  greater =[]
  lower = []

  for item in list:
    if item > pivot:
      greater.append(item)
    else:
      lower.append(item)

  return quick_sort(lower) + [pivot] + quick_sort(greater)

print(quick_sort([5,8,5,2,7,8,4,78,9,43,4,6,0]))            