# 演習１
# クラス「Monster」を作成します。
#
# このクラスには以下の関数を用意して下さい。
#
# ・set_name(self, name)：
#   引数に「name」をもらい、それをself.nameに設定する
#
# ・set_level(self, level)：
#   引数に「level」をもらい、それをself.levelに設定する
#
# ・appear(self, count)：
#   以下のように出力する
#   「レベルself.levelのself.nameがcount体あらわれた！」

class Monster:

  def set_name(self, name):
    self.name = name

  def set_level(self, level):
    self.level = level

  def appear(self, count):
    self.count = count
    print("レベル" + str(self.level) + "の" + self.name + "が" + str(count) + "体あらわれた！")
