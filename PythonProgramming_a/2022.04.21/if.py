from ast import If


ch = input("数字を入力してください")
num = int(ch)

# if, else
# if num >= 5:
#   print("結果は5以上でした。")
# else:
#   print("結果は5未満でした。")

# elif
if num == 10:
  print("10丁度です")
elif num > 10:
  print("10以上でした。")
else:
  print("10未満でした。")
