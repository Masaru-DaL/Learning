# 引数の数字２つの、それぞれの２乗の和を戻り値とする関数
def sq_plus(n1, n2):
    # Q53
    return n1 ** 2 + n2 ** 2

num1, num2 = 10, 36     # num1 と num2 に値を設定

# num1 と num2 を引数に、関数sq_plusを呼び出して、
result = sq_plus(num1, num2)

# 戻り値を result に代入する
# Q54


# result が 1000 以上 10000 未満なら「結果は４ケタです」
# そうでない場合は、「結果は４ケタではありません」と出力する
# Q55
if 1000 <= result < 10000:
    print("結果は" + str(result) + "です。４ケタです")
    print("結果は", result, "です。４ケタです")
else:
    print("結果は", result, "です。４ケタではありません")

#２３まで
