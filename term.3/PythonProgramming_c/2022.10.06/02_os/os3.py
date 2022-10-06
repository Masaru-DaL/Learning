import os

# カレントフォルダを移動する
os.chdir("./output")

# ファイルを消去する
os.remove("text2.txt")

# フォルダを消去する
os.rmdir("NewFolderNext")
