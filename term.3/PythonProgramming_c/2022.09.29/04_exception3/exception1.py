# 独自の例外クラスを作成する（例外クラスを継承する）
class Over100Error(Exception):
    def __init__(self, arg=""):
        self.arg = arg

    def __str__(self):
        return f"[{self.arg}]は100を超えています。"


class Over10000Error(Over100Error):
    def __init__(self, arg=""):
        self.arg = arg

    def __str__(self):
        return f"[{self.arg}]は10,000を超えています。"


try:
    # 数字を入力してもらう
    print("")
    num = input("数字を入力してください：")
    if int(num) > 10000:
        raise Over10000Error(num)
    if int(num) > 100:
        raise Over100Error(num)

except Over10000Error as e:
    print("Over 10,000 error")
    print(e)
except Over100Error as e:
    print("Over 100 error")
    print(e)


# except Exception as e:
#     print(type(e))z
#     print(e)
#     print("エラーが発生しました！")
