from diamond import Diamond
from rectangle import Rectangle

# 正方形クラス
class Square(Diamond, Rectangle):
    
    # コンストラクタで１辺の長さをもらい、
    # ひし形クラス、平行四辺形クラスにそれぞれ設定する
    def __init__(self, length):
        pass


