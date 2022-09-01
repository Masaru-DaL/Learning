# 演習２
# 雷クラス
class Thunder:
    
    # コンストラクタ（天気名を設定する）
    def __init__(self):
        self.t_name = "雷"
    
    # 落雷回数の設定
    def set_t_value(self, value):
        self.value = value
    
    # 情報の表示
    def thunder_info(self):
        print(f"１時間に{self.t_name}が{self.value}回落ちました。")

