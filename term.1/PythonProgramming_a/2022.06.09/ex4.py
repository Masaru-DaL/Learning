# 繰り返し演習
#
# １）1から10までの数字を出力する。
for i in range(10):
  print(i+1)


# ２）1から10までの数字を１つ飛ばしで出力する。
#    （9まで出力される）
for i in range(10):
  if i % 2 == 0:
    pass
  else:
    print(i)
