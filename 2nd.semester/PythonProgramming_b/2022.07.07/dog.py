class Dog:

    # クラス変数
    
    # コンストラクタ関数
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.favorite = ""

    # 犬の個別情報を出力する関数
    def output_info(self):
        fav = self.favorite
        if fav == "":
            fav = "不明"
        print(f"このイヌは{self.kind}の{self.name}です。")
        print(f"好きな物は{fav}です。")



