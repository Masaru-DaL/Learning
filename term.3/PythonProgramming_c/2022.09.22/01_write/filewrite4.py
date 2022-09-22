# 書き込むためにファイルを開く【フォルダを指定】
write_file = open("./folder1/text.txt", "w")
# 書込み
write_file.write("改行付きで書込み１\n")
write_file.write("改行付きで書込み２")
# ファイルを閉じる
write_file.close()
