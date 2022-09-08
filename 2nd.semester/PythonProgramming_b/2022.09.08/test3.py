class Numbers:
  NUM_LIST = [1, 2, 3, 4, 5]

  def __init__(self):
    self.i = 0

  def __iter__(self):
    return self

  def __next__(self):
    if self.i >= len(Numbers.NUM_LIST):
      raise StopIteration()

    num = Numbers.NUM_LIST[self.i] * self.i
    self.i += 1
    return num

numbers = Numbers()
for num in numbers:
  print(num, end=" ")
