
while True:
    # ファイル名を入力してもらう
    ch = input("ファイル名を入力してください：")
    # ファイルパスを作成する
    f_pass = "./output/" + ch + ".txt"
    try:
        # 書き込むためにファイルを開く（x）
        with open(f_pass, "x") as write_file:
            # 書込み
            write_file.write("ファイルを作成しました。")
    except:
        # エラーをもみ消しているため、見た目は正常に動くが
        # ちゃんと動作していないし、
        # 使っている人も、デバッグする人も分からない！
        pass
