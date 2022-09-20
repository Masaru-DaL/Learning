CAKE_STOCK = 75     # ケーキの在庫数
PIE_STOCK = 50      # パイの在庫数

CAKE_PRICE = 150    # ケーキの値段
PIE_PRICE = 120     # パイの値段

# ケーキの個数を入力
ch = input("ケーキはいくつ購入しますか？：")
cake_buy = int(ch)

# パイの個数を入力
ch = input("パイはいくつ購入しますか？：")
pie_buy = int(ch)

# ケーキの個数かパイの個数が、在庫数より多く入力された場合、
# 「在庫が足りません」と出力する。
if cake_buy > CAKE_STOCK or pie_buy > PIE_STOCK:
  print("在庫が足りません")

# そうでない場合、ケーキとパイの合計金額を出力する。
# 「合計で000円になります」
else:
  cake_sum = cake_buy * CAKE_PRICE
  pie_sum = pie_buy * PIE_PRICE
  price_sum = cake_sum + pie_sum
  print("合計で" + str(price_sum) + "円になります")
