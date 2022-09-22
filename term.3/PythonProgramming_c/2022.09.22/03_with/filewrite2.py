# 追加で書き込むためにファイルを開く（a）
write_file = open("folder1/test2.csv", "a", encoding="Shift-JIS")

# 入力待ち
ch = input("書き込む文字列：")

# 書込み
write_file.write(ch)

# ファイルを閉じる
write_file.close()


