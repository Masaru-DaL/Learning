# 書き込むためにファイルを開く【フォルダ、文字コードを指定】
write_file = open("folder1/file2.txt", "w")
# 書込み
write_file.write("改行付きで書込み１\n")
write_file.write("改行付きで書込み２\n")
# ファイルを閉じる
write_file.close()

# 書き込むためにファイルを開く【フォルダ、文字コードを指定】
write_file = open("folder1/file3.txt", "w")
# 書込み
write_file.write("改行付きで書込み１\n")
write_file.write("改行付きで書込み２\n")
# ファイルを閉じる
write_file.close()
