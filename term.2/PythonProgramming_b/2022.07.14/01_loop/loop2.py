# リスト
list_alpha_s = ['a','b','c','d','e','f','g']
list_alpha_l = ['A','B','C','D','E','F','G']


# リストの要素数だけ繰り返し
# i = 1
# for s in list_alpha_s:
#     print(f"アルファベット {i} 番目の小文字は {s} です")
#     i += 1

# for i in range(len(list_alpha_s)):
#     print(f"アルファベット {i} 番目の小文字は {list_alpha_s[i]} です")

# enumerate() -> 列挙する
# iの初期値は0, リストから入る先はs
# forの次に書く1つ目が数、2つ目が要素

for i, s in enumerate(list_alpha_s):
    print(f"アルファベット {i+1} 番目の小文字は {s} です")

# zip() -> 2つのリストをループさせる
for s, l in zip(list_alpha_s, list_alpha_l):
    print(f"アルファベット小文字だと {s}、 大文字だと {l} です")
