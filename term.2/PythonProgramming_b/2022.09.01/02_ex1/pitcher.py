# 演習１
# 投手クラス
class Pitcher:
    
    # 名前の設定
    def set_p_name(self, name):
        self.p_name = name
    
    # 防御率の設定
    def set_era(self, era):
        self.era = era
    
    # 情報の表示
    def show_p_info(self):
        print(f"{self.p_name}の防御率は{self.era}です。")

