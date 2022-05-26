

# numまでの数の総和を求める関数（引数：num）
def sum(num):
    print("関数 num が呼び出されました。")
    # num が０以下になったら、引数の num をそのまま返して関数を終了する
    if num <= 0:
        return num

    # num と、num-1を引数にした sum の実行結果を返す（再帰呼出し）
    return num + sum(num-1)

# 名前と時間を入力してもらう
input_num = int(input("整数を入力してください："))

# 関数を実行
total = sum(input_num)
print(input_num, "までの数の総和は", total, "です")
