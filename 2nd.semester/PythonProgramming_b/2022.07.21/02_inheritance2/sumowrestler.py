# 演習２
# 子クラスとなる「SumoWrestler」クラスを
# 「Sportsman」クラスを継承して作成して下さい
from sportsman import Sportsman

class SumoWrestler(Sportsman):

# このクラスには下記のメソッドを用意して下さい
# いずれも親クラスのメソッドのオーバーライドになります。
# ・set_name(self, name, ban)
# 名前と番付(ban)をインスタンス変数に設定する
# 名前は後ろに「関」を付ける
  def set_name(self, name, ban):
    self.name = name + "関"
    self.ban = ban

# ・introduction(self)
# 「彼のしこ名はｘｘです。」（改行なし）
# 「角界に入ってｘｘ年目のｏｏです。」（改行あり）と出力する
# ｏｏの部分には番付(ban)を設定する
  def introduction(self):
    print(f"彼のしこ名は{self.name}です。", end = " ")
    print(f"角界に入って{self.year}年目の{self.ban}です。")
