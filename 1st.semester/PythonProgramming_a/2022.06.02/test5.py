def sq_plus(n1, n2):
  return (n1 ** 2)+(n2 **2)

num1, num2 = 5000, 36
result = sq_plus(num1, num2)

if 1000 <= result < 10000:
  print(1)
else:
  print(2)
