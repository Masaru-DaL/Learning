# 繰り返し演習

# 数字を入力してもらう。
# "0"が入力されたら終了する
# 他の数字が入力されたら、その2乗の数字を出力して、
# 再び数字を入力してもらう
# ch = input("数字を入力してください：")
# num = int(ch)

# result = 0

# while num != 0:
#   print("0ではないので数字を2乗します")
#   num = num ** 2
#   print("現在の数字は" + str(num) + "です。")
#   ch = input("数字を入力してください：")
#   num = int(ch)
#   result = result + num
#   if num == 0:
#     print("終了します")
#     break

while True:
  ch = input("数字を入力してください")
  num = int(ch)
  if num == 0:
    break
  print(num ** 2)
