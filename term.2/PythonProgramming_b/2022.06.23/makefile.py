# osモジュールのインポート
import os
##########################################################
# 空のファイルを作る関数
# ※中身はまだ理解する必要はありません
def make_file(path):
    
    if os.path.isfile(path):
        print("エラー！！ すでにファイルが存在します！")
        return

    try:
        f = open(path, 'w')
        f.close()
    except:
        print("エラー！！ ファイルを作れませんでした！")
##########################################################

# make_file 関数で、ファイルを作成する
make_file("test.txt")

