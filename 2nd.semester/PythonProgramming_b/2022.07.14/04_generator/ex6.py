# 演習６
# 下記の３つのジェネレータ式の結果を頭の中で考えて下さい。
# それぞれについて、ジェネレータ式からデータをすべて取り出して
# 出力し、考えた結果とあっていたか確認して下さい。
# インスタンス作成時には、相手のチーム名を引数に渡します

# ジェネレータ式１
gene1 = (i*(i+1) for i in range(1, 10, 2))

print()

# ジェネレータ式２
list_num = [3, 11, 7, 1]
gene2 = (i*num for i, num in enumerate(list_num))

print()

# ジェネレータ式３
list_a = ["一石", "三寒", "五臓", "七転"]
list_b = ["二鳥", "四温", "六腑", "八倒"]
gene3 = (a + b for a, b in zip(list_a, list_b))

print()

