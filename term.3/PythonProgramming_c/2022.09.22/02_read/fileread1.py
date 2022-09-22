# 読み込むためにファイルを開く（r）
rf = open("./folder1/shiftjis.txt", "r")
# 読み込み
data = rf.read()
# ファイルを閉じる
rf.close()
# 読み込んだデータを出力
print(data)
