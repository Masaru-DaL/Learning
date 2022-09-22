# 読み込むためにファイルを開く（r）【文字コードを指定】
write_file = open("folder1/utf8.txt", "r", encoding="UTF-8")
# 行単位で読み込み（１行のみ）
line = None
# 行を出力
print(line)
print("===========") # 区切り用の線
# 読み込み行が空になるまで繰り返す
while line != '':
    # 行単位で読み込み（１行のみ）
    line = None
    # 行を出力
    print(line)

# ファイルを閉じる
write_file.close()
