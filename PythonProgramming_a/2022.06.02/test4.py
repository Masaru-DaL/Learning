list_num = []
ch = ''

while ch != '0':
  ch = input("整数を入力してください(0で終了):")

  list_num.append(int(ch))

sum = 0

sum = sum(list_num)
print(sum)
