
print("１つ目の数字／２つ目の数字を計算します。")
# 数字を２つ入力してもらう
ch1 = input("１つ目の数字を入力してください：")
ch2 = input("２つ目の数字を入力してください：")

try:
    num1 = int(ch1)
    num2 = int(ch2)
    result = num1 / num2

    print(f"{num1} / {num2} は {result}です。")

except ValueError:
    print("数字以外が入力されました。")
except ZeroDivisionError:
    print("0で割ることは出来ません。")
