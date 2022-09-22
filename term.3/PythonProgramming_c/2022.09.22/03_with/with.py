# with文を使ったファイルの書き込み
# with open("./folder1/test4.txt", "w", encoding="UTF-8"):
with open("./folder1/test4.txt", "a", encoding="UTF-8") as wf:
# 書き込むためにファイルを開く（a）

    # 書込み
    # open("./folder1/test4.txt", "w", encoding="UTF-8").write("書き込み成功")
    wf.write("書き込み成功")

# with文が終わったところで、ファイルオブジェクトが閉じられる！！
