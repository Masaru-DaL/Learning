
colors = {'red', 'orange', 'yellow'}            # 色のリスト
fruits = {'apple', 'grape', 'orange', 'peach'}  # 果物のリスト

# 和：足し合わせて重複しているものは1つにする
# |(パイプ)を使用
print(colors | fruits)

# 差：colorsだけにあるもの
print(colors - fruits)

# 積：両方にあるもの
print(colors & fruits)

# 対称差：どちらかにだけあるもの
print(colors ^ fruits)
