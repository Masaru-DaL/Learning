import datetime # 日時のモジュール
now = datetime.datetime.now() # 現在の日時の取得

print(now)

# 年月日、時分秒を表示(間に空白)
print(f"現在：{now:%Y %m %d %H %M %S}")

# 数値の後ろに年月日時分秒
print(f"現在：{now:%Y年%m月%d日%H時%M分%S秒}")
