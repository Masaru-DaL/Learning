import timeit


def func1(a, b):
    t = a
    a = b
    b = t
    return a, b


def func2(a, b):
    return b, a


x, y = 1, 2

# 関数や変数を使う場合、「globals=globals()」という指定を用いる
result1 = timeit.timeit("func1(x, y)", globals=globals())
result2 = timeit.timeit("func2(x, y)", globals=globals())


# 計測結果（かかった秒数）を出力
print(result1)
print(result2)
