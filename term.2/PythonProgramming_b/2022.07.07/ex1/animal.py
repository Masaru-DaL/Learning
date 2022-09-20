# 演習０
# クラス「Animal」（動物）を作成します。
#
# このクラスには以下の関数を用意して下さい。
#
# ・コンストラクタ(self, kind, bark)
#   引数に「kind（種類）」「bark（鳴き声）」をもらい、
#   それをそれぞれ同名のインスタンス変数に設定する
#
# ・crowing(self, times)：
#   「kindがbarkbarkbarkと鳴きました」のように
#   その動物が指定された回数鳴いた事を示す文章を出力します。
#

class Animal:
  def __init__(self, kind, bark):
    self.kind = kind
    self.bark = bark

  def crowing(self, times):
    self.times = times

    if self.times == 0:
      print(f"{self.kind}は鳴きませんでした\n")
    else:
      print(f"{self.kind}が {self.bark * times} と鳴きました\n")
