class Parent:
  def calc(self, a, b):
    return a + b

class Child(Parent):
  def calc(self, a, b):
    return a * b

c1 = Child()
result = c1.calc(3, 5)
print(result)
