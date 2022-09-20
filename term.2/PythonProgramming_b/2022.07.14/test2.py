list_num = [1, 2, 3, 4, 5]

for i, num in enumerate(list_num):
  print(i, num, "\n")
  print(i * num, end = " ")
  if i >= 3:
    break
