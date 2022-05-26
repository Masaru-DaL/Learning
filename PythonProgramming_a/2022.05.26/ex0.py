# 演習０（前回の復習）
#
# 以下の説明の関数を作成し、
# 「１～入力された数」まで繰り返し実行し、
# 結果をlist_numに順番に入れるプログラムを作成してください。

# 関数
# 引数に数値を１つ受け取る
# 引数が４の倍数なら、1/4にした整数の値を戻り値にする
# 引数が４の倍数以外なら、そのままの値を戻り値にする

def quarter_num(num):
    if num % 4 == 0:
        return num // 4
    else:
        return num


# list_num を空にする
list_num = []
# 整数を入力してもらう
num = int(input("整数を入力してください："))

# 1から入力された数まで繰り返す
for i in range(1, num + 1):
    # 結果をlist_numに入れる
    ret_num = quarter_num(i)
    list_num.append(ret_num)

# 結果を出力
print(list_num)
