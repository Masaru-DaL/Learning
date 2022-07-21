# 演習３
# 親クラスとなる「Triangle」クラスです。
# このクラスは特に修正する必要はありません。
import math         # 平方根を求めるためにimport（詳細は３学期）

class Triangle:
    
    # コンストラクタ引数として、３つの辺の長さをもらい
    # それぞれをインスタンス変数に設定する
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    # ヘロンの公式により面積を求める
    def culc_area(self):
        a = self.side1
        b = self.side2
        c = self.side3
        
        s = (a + b + c) / 2.0
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

