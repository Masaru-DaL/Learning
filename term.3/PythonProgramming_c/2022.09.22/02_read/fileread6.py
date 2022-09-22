# 読み込むためにファイルを開く（r）【文字コードを指定】
write_file = open("folder1/mapdata.txt", "r", encoding="UTF-8")
# マップデータを入れる用のリスト
mapdata = []
# 繰り返し読み込む
while True:
    # 行単位で読み込み（１行のみ）
    line = write_file.readline()
    # １行データの余計な文字（先頭、末尾の空白や改行）を取り除く
    line = ''
    # 読み込み行が空になったら終了
    if line == '':
        break
    
    # 行を出力
    print(line)
    # 行をカンマで分割
    data = None
    # マップデータを出力
    print(data)
    # マップデータに追加
    mapdata.append(data)

# ファイルを閉じる
write_file.close()
# マップデータを出力
print(mapdata)

