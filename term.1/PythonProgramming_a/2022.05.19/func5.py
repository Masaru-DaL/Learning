# 時、分、秒から、秒数を計算する
def culc_seconds(hour, minute, second):
    minutes = hour * 60 + minute    # 分数
    seconds = minutes * 60 + second # 秒数
    return minutes # 計算した分を戻り値にする
    # return seconds # 計算した秒を戻り値にする

hour, minute, second = 3, 20, 50
time = culc_seconds(hour, minute, second)
print(hour,"時間",minute,"分",second,"秒は、",time,"秒です")
