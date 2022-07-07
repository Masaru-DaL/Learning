# 演習４
# クラス「Gacha」を作成します。
# クラス変数として以下の２つを用意して下さい
# tenjo （レアが出ない上限回数となる数）
# no_rare_count（連続してレアが出てない数）
import random

class Gacha:

    tenjo = 10
    no_rare_count = 0
    # このクラスには以下の関数を用意して下さい。
    # ・コンストラクタ(self, name, percent)
    #   引数に「name」「percent」をもらい、
    #   それをそれぞれインスタンス変数に設定する
    def __init__(self, name, percent):
        self.name = name
        self.percent = percent

    # ・roll_gacha(self)
    #   random.random() 関数で0～1までの小数値を取得する
    #   取得した結果が「self.percent / 100」以下の場合、
    #   「=========レアが出ました！！！！！！」と出力し、
    #   クラス変数のno_rare_countを0にする
    #   取得した結果が「self.percent / 100」より大きいの場合、
    #   「---------ノーマルでした」と出力し、
    #   クラス変数のno_rare_countを1増やす
    def roll_gacha(self):
        num = random.random()

        if num <= self.percent / 100:
            print(f"=========レアが出ました！！！！！！")
            Gacha.no_rare_count = 0

        elif num >= self.percent /100:
            print(f"---------ノーマルでした")
            Gacha.no_rare_count += 1


    # info_tenjo(cls) ※クラスメソッド
    #   クラス変数の情報を出力する
    #   「天井：tenjo、現在回数：no_rare_count」
    @classmethod
    def info_tenjo(cls):
        print(f"天井：{Gacha.tenjo}, 現在回数：{Gacha.no_rare_count}")

    # is_tenjo(cls) ※クラスメソッド
    #   クラス変数の no_rare_count が tenjo 以上だったらTrueを、
    #   そうでない場合はFalseを戻り値として返す
    @classmethod
    def is_tenjo(cls):
        if Gacha.no_rare_count > Gacha.tenjo:
            return True
        else:
            return False
