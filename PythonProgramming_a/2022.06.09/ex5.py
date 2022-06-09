# 繰り返し演習

list_a = ["a","b","c","d","e","f"]
# １）list_a の要素の文字を順にすべて出力する。
i = 0
for element in list_a:
  if i < len(list_a):
    print(str(i) + "番目は" + str(element) + "です")
    i = i + 1
# ２）list_a の要素を「0番目はaです」のようにすべて出力する
