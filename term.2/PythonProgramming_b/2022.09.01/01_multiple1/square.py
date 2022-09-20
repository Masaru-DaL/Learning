from diamond import Diamond
from rectangle import Rectangle

# 正方形クラス
class Square(Diamond, Rectangle):

    # コンストラクタで１辺の長さをもらい、
    # ひし形クラス、長方形クラスにそれぞれ設定する
    def __init__(self, length):
        self.set_side_length(length)
        self.set_height(length)
        self.set_width(length)
