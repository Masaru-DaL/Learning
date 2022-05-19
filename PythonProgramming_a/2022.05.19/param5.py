# ローカル変数の確認
def test_local(num1, num2):
    answer = num1 + num2

answer = 0
num1, num2 = 3, 4
test_local(num1, num2)
print(answer)

