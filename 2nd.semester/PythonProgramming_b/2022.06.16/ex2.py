# 演習２

# 数字を２つ入力してもらい、
# 「１つ目の数 割る ２つ目の数」と
# 「２つ目の数 割る １つ目の数」を出力します。

# 現在のプログラムでも正しく動作するのですが、
# 「数字じゃない値」や「０」を入力されると
# エラーとなってしまいます。
# その場合にユーザにメッセージを出して、
# エラーとせずに再度入力してもらうように修正してください。
# 初めて登場しますが「isdigit」を利用すると良いでしょう。

# 正の整数を入力してもらう

str_num1 = input("正の整数（１つめ）を入力してください：")
str_num2 = input("正の整数（２つめ）を入力してください：")

while True:
  # 標準ライブラリの組み込み関数「isdigit()」を使用すると
  # その文字がすべて数字か分かる（すべて数字ならTrue）
  num1_flag = str_num1.isdigit()
  num2_flag = str_num2.isdigit()

  if num1_flag == False or num2_flag == False:
    print("正の整数を入力してください")
    continue

  # それぞれの入力文字を数値化
  num1 = int(str_num1)
  num2 = int(str_num2)

  if num1 == 0 or num2 == 0:
    print("正の整数を入力してください")
    continue

  # 割り算した結果を表示
  print("「" + str_num1 + "/" + str_num2 + "」は" + str(num1 / num2) + "です。")
  print("「" + str_num2 + "/" + str_num1 + "」は" + str(num2 / num1) + "です。")
  break
