# 演習３
# ※提示されているフローチャートをプログラムにしてください。

# 3回繰り返す
for i in range(3):
  ch = input()

# 数値に変換する
  num = int(ch)

# num 割る 3 の余りは 0?
  if num % 3 == 0:
    print('3の倍数')

  else:
    print('割り切れません')
