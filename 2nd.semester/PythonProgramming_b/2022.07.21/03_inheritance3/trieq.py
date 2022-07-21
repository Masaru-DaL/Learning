# 演習３
# 子クラスとなる正三角形のクラス「TriEq」クラスです。
# ※「Equilateral triangle」が長いので省略してます
# 親クラスとなる「Triangle」クラスを継承して作成して下さい
from triangle import Triangle

class TriEq(Triangle):

# このクラスには下記のメソッドを用意して下さい
# ・コンストラクタ(self, side)
# 親クラスのコンストラクタを呼ぶ（実行する）、
# その際の引数は３つともに「side」を指定する
# また、引数のside（辺の長さ）をインスタンス変数に設定する
  def __init__(self, side):
    super().__init__(side, side, side)
    self.side = side

# ・info_area(self)
# 「この正三角形の面積はｘｘです。（１辺：ｏｏ）」と出力する。
# このｘｘの部分には親クラスのculc_area()メソッドを実行した
# 結果を設定します（できれば、小数点以下２ケタに調整してください）
# ｏｏの部分には、１辺の長さを設定して下さい
  def info_area(self):
    # a = self.culc_area()
    print(f"この正三角形の面積は{self.culc_area():.2f}です。(1辺：{self.side})")
