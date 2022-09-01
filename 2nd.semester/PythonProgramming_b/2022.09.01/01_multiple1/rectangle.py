# 長方形クラス
class Rectangle:
    
    # 幅を設定する
    def set_width(self, width):
        self.width = width
        
    # 高さを設定する
    def set_height(self, height):
        self.height = height
        
    # 面積を計算する
    def culc_area(self):
        return self.width * self.height

