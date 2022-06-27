# 演習１

# 定数（変わらない数字）１つ
from email.charset import BASE64


BASE_NUMBER = 25

# 整数を入力してもらい、num に代入
num = int(input("整数を入力してください："))

# ※以下のプログラム部分を書いて下さい

# ５回繰り返す
for i in range(5):
    # num に BASE_NUMBER を加算する
    num += BASE_NUMBER
    # numを出力する
    print(num)
