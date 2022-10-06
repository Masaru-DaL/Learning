# 演習１
# 繰り返し「フォルダ名」を入力してもらい、
# 入力されるたびに「exoutput」フォルダの中にフォルダを作成してください。
# 空文字（入力なし）でプログラムを終了し、
# 最後に「exoutput」フォルダの中にあるファイル／フォルダの一覧を
# ターミナルに出力してください。
#
# 可能なら例外処理を入れて、フォルダ作成でエラーとなった場合も
# 繰り返せるようにしてください。
import os

while True:
    folder_name = input("フォルダ名を入力してください：")

    if folder_name == "":
        break

    os.mkdir("./exoutput/" + folder_name)

folder_list_name = os.listdir("./exoutput")
print(folder_list_name)
