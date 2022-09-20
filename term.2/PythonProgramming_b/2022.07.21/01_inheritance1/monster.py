# モンスタークラス
class Monster:
    
    # 名前を設定
    def set_name(self, name):
        self.name = name
        
    # 攻撃（文章のみ）
    def attack(self):
        print(self.name + "は攻撃した！")
        
        