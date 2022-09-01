# 演習２
# 雨クラス
class Rain:
    
    # コンストラクタ（天気名を設定する）
    def __init__(self):
        self.r_name = "雨"
    
    # 降水量の設定
    def set_r_value(self, value):
        self.value = value
    
    # 情報の表示
    def rain_info(self):
        print(f"１時間に{self.r_name}が{self.value}mm降りました。")

