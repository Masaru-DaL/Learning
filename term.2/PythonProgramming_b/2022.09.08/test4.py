list_num = [1, 2, 3]

gene = (i * 2 for i in list_num)

for g in gene:
  print(g, end=" ")
