# ローカル変数の確認
def print_result(name, subject, score):
    print(name+"さんの"+subject+"の点数は"+str(score)+"点です")

print_result(score = 80, subject = "数学", name = "太郎")
print_result("二郎", score = 75, subject = "英語")
