# 演習２

# 整数を２つ入力してもらいます。
# 「１つ目の数字」割る「２つめの数字」の答えを、
# 小数点以下２ケタまで表示してください。

num1 = int(input("整数を入力してください："))
num2 = int(input("整数をもうひとつ入力してください："))

print('{:.2f}'.format(num1 / num2))

result = num1 / num2
print(f"{result:.2f}")


