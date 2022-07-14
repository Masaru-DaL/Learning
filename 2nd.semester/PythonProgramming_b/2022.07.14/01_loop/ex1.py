# 演習１
# 
# ランダムに１つの「アウト！」かたくさんお「セーフ」から選び、
# 選ぶたびにその要素がなくなっていくリストがあります。
#
# 「アウト！」が出る前に「n で終了した場合のみ」、
# 「あなたは、count回の生き残りに成功しました！」と
# メッセージが出るようにして下さい。
# ※「アウト！」が出てしまった場合は容赦なく、回数は表示しないで下さい
import random

STR_OUT = "アウト！"

data_list = ["セーフ"] * 20
data_list.append(STR_OUT)
random.shuffle(data_list)

yameru = False
count = 0
while yameru == False:
    
    ch  = input("まだ続けますか？ n で終了：")
    if ch == 'n':
        yameru = True
    else:
        idx = random.randint(0, len(data_list) - 1)
        result = data_list.pop(idx)
        print(result)
        if result == STR_OUT:
            break
        count += 1
