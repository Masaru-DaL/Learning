class Dog:

    # クラス変数
    dog_count = 0
    last_dog_name = ""


    # コンストラクタ関数
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.favorite = ""
        Dog.dog_count += 1
        Dog.last_dog_name = self.name

    # 犬の個別情報を出力する関数
    def output_info(self):
        fav = self.favorite
        if fav == "":
            fav = "不明"
        print(f"このイヌは{self.kind}の{self.name}です。")
        print(f"好きな物は{fav}です。")

    @classmethod
    def collection_info(cls):
        print(f"現在{cls.dog_count}匹の犬がいます。")
