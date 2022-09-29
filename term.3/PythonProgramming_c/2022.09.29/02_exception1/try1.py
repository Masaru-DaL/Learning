# このファイルには、演習０のプログラムをコピーしてください。
make_file = input("ファイル名を作成してください：")
# ファイルパスを作成する
file_pass = "./output/" + make_file + ".txt"

try:
    # 書き込むためにファイルを開く（x）
    with open(file_pass, "x") as mf:
        # 書込み
        mf.write("ファイルを作成しました。")

except FileExistsError as e:
    print("【エラー！】すでに同じ名前のファイルが作成されています！")
    print(type(e))
    print(e)
