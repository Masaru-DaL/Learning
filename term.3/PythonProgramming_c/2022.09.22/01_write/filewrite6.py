# それぞれのファイルに追加書込みをしてみる
# 書き込むためにファイルを開く【フォルダを指定】
write_file = open("folder1/file2.txt", "a")
# 書込み
write_file.write("追加書込み\n")
# ファイルを閉じる
write_file.close()

# 書き込むためにファイルを開く【フォルダを指定】
write_file = open("folder1/file3.txt", "a")
# 書込み
write_file.write("追加書込み\n")
# ファイルを閉じる
write_file.close()

