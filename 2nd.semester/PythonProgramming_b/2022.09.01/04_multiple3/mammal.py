# 哺乳類クラス
class Mammal:
    
    # コンストラクタで名前の初期化
    def __init__(self):
        self.name_mam = ""
        print("Mammal init")
    
    # 名前の設定
    def set_name(self, name):
        self.name_mam = name
        
    # 情報の表示
    def show_info_mam(self):
        if self.name_mam == "":
            print("※まだ名前が未設定です！")
        else:
            print(self.name_mam + "は肺で呼吸します")

