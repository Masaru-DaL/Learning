# 演習６
# 下記の３つのジェネレータ式の結果を頭の中で考えて下さい。
# それぞれについて、ジェネレータ式からデータをすべて取り出して
# 出力し、考えた結果とあっていたか確認して下さい。
# インスタンス作成時には、相手のチーム名を引数に渡します

# ジェネレータ式１
# 1~10まで2つ数字を飛ばしてiが出力される(1, 3, 5, 7, 9)
gene1 = (i*(i+1) for i in range(1, 10, 2))
for d in gene1:
  print(d, end=" ")

print()
# ジェネレータ式２
# enumerate() -> 0~ iを取ってくる
list_num = [3, 11, 7, 1]
gene2 = (i*num for i, num in enumerate(list_num))

for d in gene2:
  print(d, end=" ")

print()
# ジェネレータ式３
list_a = ["一石", "三寒", "五臓", "七転"]
list_b = ["二鳥", "四温", "六腑", "八倒"]
gene3 = (a + b for a, b in zip(list_a, list_b))

for i in gene3:
  print(i, end = " ")
print()
