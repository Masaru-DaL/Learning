
# ジェネレータ式
doubles = (i*i for i in range(10))
print(type(doubles))

print()


list_x = [10, 20, 30]
list_y = [7, 5, 3]

multi = (x*y for x, y in zip(list_x, list_y))  

print()


doubles2 = [i*i for i in range(10)]

