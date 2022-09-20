from monster import Monster

# ゴーレムクラス(モンスタークラスを継承)
class Golem(Monster):

  def __init__(self):
    self.set_name("ゴーレム")

  def defense(self):
    print(self.name + "は防御している")
