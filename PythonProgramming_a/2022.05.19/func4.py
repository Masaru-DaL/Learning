
def print_number(input_num):
    for i in range(0, 101):
        print(i, end=" ")
        if i == input_num:
            print()
            return
    print("数字を最後まで表示しました")

while True:
    ch = input("数字を入力してください（０で終了）：")
    num = int(ch)
    if num == 0:
        break
    print_number(num)



