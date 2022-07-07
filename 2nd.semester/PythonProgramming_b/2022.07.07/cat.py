class Cat:

    # コンストラクタ関数
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.favorite = ""

    # 猫の個別情報を出力する関数
    def output_info(self):
        fav = self.favorite
        if fav == "":
            fav = "不明"
        print(f"このネコは{self.kind}の{self.name}です。")
        print(f"好きな物は{fav}です。")

    # 名前を取得する関数

