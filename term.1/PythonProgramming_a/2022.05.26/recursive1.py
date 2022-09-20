
# あいさつ文を出力する関数
def output_greeting(name, hour, msg):
    print(str(hour) + "時ですね、" + name + "さん、" + msg)

# あいさつ関数
def greeting(name, hour):
    if 5 <= hour and hour <= 11:
        output_greeting(name, hour, "おはようございます。")
    elif 12 <= hour and hour <= 17:
        output_greeting(name, hour, "こんにちは。")
    else:
        output_greeting(name, hour, "こんばんは。")

# 名前と時間を入力してもらう
name = input("名前を入力してください：")
hour = int(input("時間（0時～23時）を入力してください："))
# 関数を実行
greeting(name, hour)
