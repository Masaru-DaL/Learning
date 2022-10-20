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



# 計測結果（かかった秒数）を出力
print(result1)
print(result2)


