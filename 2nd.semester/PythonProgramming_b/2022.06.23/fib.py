# フィボナッチ数列リストを返す関数
def fib_ret(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == "__main__":

    # 動作確認用プログラム
    num = int(input("数字を入力："))
    print(fib_ret(num))
