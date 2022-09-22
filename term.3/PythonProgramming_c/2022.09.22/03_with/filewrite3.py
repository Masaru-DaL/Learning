# 入力待ち
ch = input("書き込む文字列：")

# 追加で書き込むためにファイルを開く（a）
write_file = open("folder1/test3.csv", "a", encoding="Shift-JIS")

# 書込み
write_file.write(ch)

# ファイルを閉じる
write_file.close()


