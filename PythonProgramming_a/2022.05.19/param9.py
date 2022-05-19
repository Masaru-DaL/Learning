# ローカル変数の確認
def print_result(name, subject = "数学", score = 0):
    print(name+"さんの"+subject+"の点数は"+str(score)+"点です")

print_result("太郎")
print_result(name = "二郎", score = 75)

