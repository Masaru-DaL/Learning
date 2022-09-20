import fib      # fib モジュールをインポート

while True:
    # ユーザへの説明メッセージ
    print("整数を入力してください。")
    print("その数までのフィボナッチ数列を出力します。")
    num_str = input("整数を入力：")

    if not(num_str.isdecimal()):
        print("整数以外が入力されました。")
        continue
    
    num = int(num_str)
    result = fib.fib_ret(num)
    print("結果を出力します。")
    print(result)
    break



