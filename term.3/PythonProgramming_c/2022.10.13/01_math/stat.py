import statistics

data = [1, 4, 5, 4, 2, 4, 2, 1]

# データ表示
print(f"データは{data}です")
# 【statistics.mean】（相加）平均
print(f"平均値は{statistics.mean(data)}です")
# 【statistics.median】中央値
print(f"中央値は{statistics.median(data)}です")
# 【statistics.mode】最頻値
print(f"最頻値は{statistics.mode(data)}です")

# 【statistics.variance】分散
print(f"分散は{statistics.pvariance(data)}です")
# 【statistics.stdev】標準偏差
print(f"標準偏差は{statistics.pstdev(data)}です")
