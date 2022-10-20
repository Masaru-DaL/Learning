import timeit

# 合計値計算関数１
def func1(nums):
    total = 0
    for i in nums:
        total += i
    return total


# 合計値計算関数２
def func2(nums):
    return sum(nums)


# 1から10000までのリストを作る
num_list = [i for i in range(1, 10001)]

# 演習１
# 下記のプログラムは、それぞれ「関数１」「関数２」「関数を使わずにそのままsumで計算」
# としたもので結果は同じです。それぞれにかかる時間をtimeitで出力してください。
# すべて、実行回数は「１万回」を指定してください。
result1 = timeit.timeit("func1(num_list)", globals=globals(), number=10000)
result2 = timeit.timeit("func2(num_list)", globals=globals(), number=10000)
result3 = timeit.timeit("sum(num_list)", globals=globals(), number=10000)

print(func1(num_list))
print(func2(num_list))
print(sum(num_list))
print("----------------")


# 計測結果（かかった秒数）を出力
print(result1)
print(result2)
print(result3)
