# ひし形クラス
class Diamond:
    
    # １辺の長さを設定する
    def set_side_length(self, side):
        self.side  = side 
        
    # 周りの長さを計算する
    def culc_perimeter(self):
        return self.side * 4


