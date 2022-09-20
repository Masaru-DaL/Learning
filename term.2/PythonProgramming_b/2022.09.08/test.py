class Number:
  a = 1

  def set_num(self, num):
    self.num = num
    Number.a = num

num1 = Number()
num2 = Number()
num1.set_num(5)
num2.set_num(6)
print(num1.a)
