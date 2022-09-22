# 読み込むためにファイルを開く（r）【文字コードを指定】
write_file = open("folder1/utf8.txt", "r")
# 読み込み
data = write_file.read()
# ファイルを閉じる
write_file.close()
# 読み込んだデータを出力
print(data)

