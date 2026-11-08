def splitter(list_nums : list):
  odd = []
  even = []
  for i in list_nums:
    if i % 2 == 0:
      even.append(i)
    else:
      odd.append(i)
  print (odd)
  print (even)


splitter([12, 7, 34, 21, 5, 10, 8, 3, 19, 2])