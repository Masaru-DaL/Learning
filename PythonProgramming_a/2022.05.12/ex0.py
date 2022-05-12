# 演習０（前回の復習）
# ※コメントを参照して、プログラムの不足箇所を埋めてください
#
# タプルにデータが入っています。
# これをソートして順番に出力したいのですが、
# タプルは値を変更することが出来ません。
# リストに１つ１つデータを移して、ソートして出力して下さい。
#
# 入出力例（途中まで）
# 【メニュー一覧】
# baumkuchen
# cheese cake
# chiffon cake


# タプルのデータ（ケーキの種類）
tuple_cakes = ('cheese cake','pound cake','chiffon cake','mille-feuille','mont blanc','gateau chocolat','tiramisu','baumkuchen')

# 空のリストを用意
cakes_list = []

# タプルのデータの数だけ繰り返し
for cake in tuple_cakes:

    # リストにデータを追加
    cakes_list.append(cake)
# リストをソート
cakes_list.sort()

# 【メニュー一覧】を出力
print(cakes_list)
# リストのデータの数だけ繰り返し
for cake in cakes_list:

    # データを１つずつ出力
    print(cake)

for i in range(len(cakes_list)):
    print(cakes_list[i])
