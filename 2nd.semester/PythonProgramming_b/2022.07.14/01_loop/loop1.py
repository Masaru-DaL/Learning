# 数値を入れるリスト
list_num = []

# 5回繰り返し
for i in range(5):
    # 数字を入力してもらう
    num = int(input(f"0以外の数字を5つ入力して下さい（{i+1}つめ）："))
    # 0ならば終了でbreak
    if num == 0:
        print("0が入力されました")
        break
    # 数をリストに追加
    list_num.append(num)
    
# 積を求めて出力
multi = 1
for i in list_num:
    multi *= i
print(f"5つの数の積は{multi}です")

