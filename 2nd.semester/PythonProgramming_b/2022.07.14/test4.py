list_num = [1, 2, 3]
gen = (i * i for i in list_num)

for g in gen:
  print(g, end = " ")
