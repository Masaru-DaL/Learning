# フィボナッチ数列のモジュール

# 特に使用しませんが、あとの説明の時に使うためのリスト
list_a = []

# フィボナッチ数列を出力する関数
# n ：出力する最大の数
def fib_print(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# フィボナッチ数列を返却する関数
# n ：返却する最大の数
def fib_return(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


