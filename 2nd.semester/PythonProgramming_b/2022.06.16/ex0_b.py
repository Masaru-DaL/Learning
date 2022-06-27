# 演習０のｂ

# 文字列を１つ入力してもらいます
# その同じ文字列を、「文字列の長さ」の回数出力します。
# ※文字列の長さを求める関数は「len()」です

# 例：入力が「abc」なら下記のように出力
# abc
# abc
# abc

# 続きのプログラムを書いて下さい

str_input = input("文字列を入力してください：")
for i in range(len(str_input)):
  print(str_input)
