# 演習０
# Star（星）クラスを継承するクラス
# Satellite（衛星）クラスを作成してください。
#
# 各メソッドは下記の説明に添って作成してください。
from star import Star
# 惑星クラス（Starクラスを継承すること）
class Satellite(Star):

    # コンストラクタ
    # 引数に星の名前をもらい、親クラスのコンストラクタを呼び出す
    def __init__(self, name):
        super().__init__(name)

    # 母惑星の設定（set_mother）
    # 引数に母惑星の名前をもらい、インスタンス変数に設定する
    def set_mother(self, mother):
        self.mother = mother

    # 情報表示（print_info）
    # 親クラスの情報表示メソッドを実行する
    # その後、このインスタンスが持つ母惑星の情報を以下のように表示する。
    # 「ｘｘの周りをまわっている衛星です。」
    def print_info(self):
        super().print_info()
        print(f"{self.mother}の周りをまわっている衛星です。")
