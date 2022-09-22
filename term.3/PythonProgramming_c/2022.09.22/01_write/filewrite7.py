# 複数行書込み
# 書き込む文字のリスト
seasons1 = ["春", "夏", "秋", "冬"]
seasons2 = ["spring", "summer", "autumn", "winter"]

# 書き込むためにファイルを開く【フォルダを指定】
write_file = open("folder1/file4.txt", "a")
# 書込み
write_file.writelines(seasons1)
# ファイルを閉じる
write_file.close()

# 書き込むためにファイルを開く【フォルダを指定】
write_file = open("folder1/file4.txt", "a")
# 改行コードのみ書込み
write_file.writelines('\n')
# 繰り返して書込み（改行コードを最後に付ける）
for season in seasons2:
    write_file.write(season + '\n')
# ファイルを閉じる
write_file.close()

