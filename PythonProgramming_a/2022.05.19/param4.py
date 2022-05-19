# ローカル変数の確認
def test_local(num1, num2):
    list_num.append(num1 + num2)

list_num = []
num1, num2 = 3, 4
test_local(num1, num2)
print(list_num)

