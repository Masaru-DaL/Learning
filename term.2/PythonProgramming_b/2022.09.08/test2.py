class Info:
  num1 = 2

  def set_num(self, num):
    self.num2 = num

  def print_info(self):
    print(f"num1 * num2 = {Info.num1 * self.num2}")

i1 = Info()
i1.set_num(4)
i1.print_info()
