# 演習１
# 打者クラス
class Batter:
    
    # 名前の設定
    def set_b_name(self, name):
        self.b_name = name
    
    # 打率の設定
    def set_average(self, average):
        self.average = average
    
    # 情報の表示
    def show_b_info(self):
        print(f"{self.b_name}の打率は{self.average}です。")

