import math

#nums = "3.5 5 18 -4 9"
nums = input("空白で区切って、複数の数字を入力してください：")

c_list = nums.split(" ")
f_list = []
i_list = []
for c in c_list:
    f = float(c)
    i = int(math.floor(f))
    f_list.append(f)
    i_list.append(i)
print(f"入力値：{f_list}")
print(f"入力値：{i_list}")

# 【math.pow】xのy乗を返す（先頭２つの数字で実施）
# 引数を４つにすると、xのy乗をzで割ったあまりらしいですが…
if len(f_list) > 1:
    print(f"{f_list[0]}の{f_list[1]}乗は{0}です。")

# 組み込み関数
# 【max】最大の数を返す（イレータブルの値か、カンマで区切って複数指定できる）
print(f"最大の数は{0}です。")
# 【min】最小の数を返す（イレータブルの値か、カンマで区切って複数指定できる）
print(f"最大の数は{0}です。")
# 【sum】合計の数を返す（イレータブルの値を指定できる）
print(f"総和は{0}です。")

# 【math.prod】すべての積の数を返す（イレータブルの値を指定できる）
print(f"すべての積は{0}です。")
# 【math.gcd】最大公約数を返す（整数のみ）
# ※カンマで区切って複数指定できる。
#　 イレータブルの値を指定する場合は先頭に*を付ける
print(f"（整数部分の）最大公約数は{0}です。")
# 【math.lcm】最大公倍数を返す（gcdと同様、Python3.9から）
print(f"（整数部分の）最大公公倍数は{0}です。")

