import os

# カレントフォルダを移動する
os.chdir("./output")

# ファイル名を変更する
os.rename("test1.txt", "text2.txt")

# フォルダ名を変更する
os.rename("NewFolder", "NewFolderNext")
