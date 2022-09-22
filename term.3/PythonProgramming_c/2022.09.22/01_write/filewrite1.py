# 書き込むためにファイルを開く（w）
write_file = open("firstfile.txt", "w")
# 書込み
write_file.write("書き込み成功")
# ファイルを閉じる
write_file.close()
