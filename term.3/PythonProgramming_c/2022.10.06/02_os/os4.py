import os

# カレントフォルダを移動する

# ファイル・フォルダのリストを取得する
f_list = os.listdir()
print(f_list)
print("--------------------")

f_list2 = os.listdir("output")
print(f_list2)
