import calendar
from operator import truediv # カレンダーモジュール

print("年、月を入力してください。")
print("月を省略すると、1年分が表示されます。")

year = int(input("西暦で年を入力してください："))
month = input("月を入力してください：")

# 月が入力された場合
if len(month) != 0:
# if month != "":
  print(calendar.month(year, int(month)))
  print(str(year) + "年の" + month +"月を出力しました。")
# 月が入力されなかった場合
else:
  print(calendar.prcal(year))
  # if calendar.isleap(year) == True:
  if calendar.isleap(year):
    print("月が省略されたので、" + str(year) + "年だけを出力しました。" + str(year) + "年は、うるう年です。")
  else:
    print("月が省略されたので、" + str(year) + "年だけを出力しました。" + str(year) + "年は、うるう年ではありません。")


# 月が入力されなかった場合
# if len(month) == 0:
#   print(calendar.prcal(year))
#   print(calendar.isleap(year))
# else:
#   print(calendar.month(year, int(month)))
