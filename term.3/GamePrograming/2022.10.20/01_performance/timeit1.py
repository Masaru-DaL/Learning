import timeit

# 小さな処理を計測するのに便利な「timeit」モジュール
# ３ステップを経て、データを入れ替える
# timeit("入れ替え方法", "変数の値")

# 2種類の方法でaとbの値を入れ替える
result1 = timeit.timeit("t=a; a=b; b=t", "a=1; b=2")
# swapを用いて、データを入れ替える
result2 = timeit.timeit("a,b = b,a", "a=1; b=2")

# 計測結果（かかった秒数）を出力
print(result1)
print(result2)
print("-------")

# 小さな処理を計測するのに便利な「timeit」モジュール
# ３ステップを経て、データを入れ替える
# numberで計測回数を指定できる: デフォルトでは100万回計測する
result1 = timeit.timeit("t=a; a=b; b=t", "a=1; b=2", number=1000000000)
# swapを用いて、データを入れ替える
result2 = timeit.timeit("a,b = b,a", "a=1; b=2", number=100000000)
# 計測結果（かかった秒数）を出力
print(result1)
print(result2)
print("-------")
