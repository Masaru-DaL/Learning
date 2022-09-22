# 読み込むためにファイルを開く（r）【文字コードを指定】
write_file = open("folder1/utf8.txt", "r", encoding="UTF-8")
# ファイルオブジェクトを for 文で繰り返す
for line in write_file:
    # 行を出力
    print(line)

# ファイルを閉じる
write_file.close()
