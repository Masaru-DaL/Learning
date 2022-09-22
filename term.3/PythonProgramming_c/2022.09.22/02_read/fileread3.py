# 読み込むためにファイルを開く（r）【文字コードを指定】
write_file = open("folder1/utf8.txt", "r", encoding="UTF-8")
# 行単位で読み込み(改行コード込み)
data = write_file.readlines()
# ファイルを閉じる
write_file.close()
# 読み込んだデータを出力
print(data)
print("===========") # 区切り用の線

# データをリストとして繰り返して出力
for line in data:
    print(line)
