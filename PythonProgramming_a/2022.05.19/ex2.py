# 演習２（関数の基本）
# 数値の引数をふたつ受け取り、
# その２つの「和」と「差」の「積」を計算し、
# 戻り値とする関数を作成して下さい。
# 例：２と３が引数なら、５かける－１＝－５が返される
#
# 作った関数を、好きな数を引数として実行して、
# 戻ってきた値を出力（数値のみでOK)してください。
# def total(num1, num2):
#   addition = int(num1 + num2)
#   subtraction = int(num1 - num2)
#   multiplication = addition * subtraction
#   print(multiplication)

# total(10, 10)

def calc_num(num1, num2):
  result = (num1 + num2) * (num1 - num2)
  return result

result2 = calc_num(5, 3)
print(result2)


# ２つの数の「和」と「差」の「積」を計算する



# 作成した関数を実行
