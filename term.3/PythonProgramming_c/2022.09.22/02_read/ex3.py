# 演習３
# 「folder2」のフォルダに「ex3.txt」というファイルがあります。
# このファイルは「utf-8」で文字が書かれています。
#
# このファイルに対して、以下の処理を行うプログラムを作成してください。
# １）読み込むためにファイルをオープンする
rf = open("./folder2/ex3.txt", "r", encoding="UTF-8")
# ２）１行読み込む
while True:
    line = rf.readline()
    # ３）読み込んだ行の先頭、末尾の空白と改行を取り除く
    data = line.strip()
    # ４）取り除いたものを（ターミナルに）出力する（通常どおり改行する）
    print(data)
    # ５）２～４）をファイルの最後まで繰り返す
    if data == "":
        break
        rf.close()

# for line in rf:
#     data = line.strip()
#     print(data)
