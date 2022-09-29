# 独自の例外クラスを作成する（例外クラスを継承する）





try:
    # 数字を入力してもらう
    print("")
    num = input("数字を入力してください：")

except Exception as e:
    print(type(e))
    print(e)
    print("エラーが発生しました！")

