# 海の生き物クラス
class SeaAnimal:
    
    # コンストラクタで名前の初期化
    def __init__(self):
        self.name_sea = ""
        print("SeaAnimal init")

    # 名前の設定
    def set_name(self, name):
        self.name_sea = name
        
    # 情報の表示
    def show_info_sea(self):
        if self.name_sea == "":
            print("※まだ名前が未設定です！")
        else:
            print(self.name_sea + "は海の中で生活します")

