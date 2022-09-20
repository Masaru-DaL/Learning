# 関数の基本3
# 引数を複数指定
def culc_price(apple_cnt, orange_cnt):
    amount = apple_cnt * 120 + orange_cnt * 80
    print("リンゴ", apple_cnt, "個とオレンジ", orange_cnt, "個の", end="")
    print("合計金額は", amount, "円です。")

culc_price(5, 8)
culc_price(2, 10)
