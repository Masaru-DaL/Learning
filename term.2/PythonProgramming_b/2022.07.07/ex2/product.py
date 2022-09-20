# 演習２
# クラス「Product」（商品）を作成します。
#
# このクラスには以下のクラス変数を用意して下さい。
# total_sell
# 総売上、初期値は0
#
# このクラスには以下の関数を用意して下さい。
#
# ・コンストラクタ(self, name, price)
#   引数に「name（名前）」「price（価格）」をもらい、
#   それをそれぞれself.name、self.priceに設定する
#
# ・sell(self)：
#   商品が（１つ）売れた事をメッセージ出力する。
#   （金額と商品名も出力する）
#   self.price を total_sell に加算する
#   （総売上を商品の金額分プラスする）
#
#  ※商品の売り切れなどは考慮しません

class Product:
  total_sell = 0
  total_num = 0

  def __init__(self, name, price):
    self.name = name
    self.price = price
    Product.total_sell += self.price
    Product.total_num += 1

  def sell(self):
    print(f"{self.name}が売れました。金額は{self.price}円です。")
