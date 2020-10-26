def bubble(list):
  indexing_length = len(list) - 1
  sorted = False

  while not sorted:
    sorted = True
    for i in range(0, indexing_length):
      if list[i] > list[i+1]:
        sorted = False
        list[i], list[i+1] = list[i+1], list[i]
  return list

print(bubble([6,2,4,9,4,21,5,8,3,6,8,14,39,33,1,6,99,4,3,228])) 