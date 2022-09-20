# 演習２
# 親クラスとなる「Sportsman」クラスです。
# このクラスは特に修正する必要はありません。
class Sportsman:
    
    # 名前をインスタンス変数に設定する
    # 名前は後ろに「さん」を付ける
    def set_name(self, name):
        self.name = name + "さん"
    
    # 経験年数をインスタンス変数に設定する
    def set_year(self, year):
        self.year = year
    
    # 「彼の名前はｘｘです。」（改行なし）
    # 「この世界に入ってｘｘ年目です。」（改行あり）と出力する
    def introduction(self):
        print(f"彼の名前は{self.name}です。", end="")
        print(f"この世界に入って{self.year}年目です。")

