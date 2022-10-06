import os

# カレントフォルダを移動する
os.chdir("./output/")

# 指定のフォルダを作成する
os.mkdir("NewFolder")

# 指定のフォルダの中に、指定のフォルダを作成する
os.mkdir("temp/NewFolder")
