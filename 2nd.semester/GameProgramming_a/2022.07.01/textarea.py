import tkinter
from tokenize import TokenInfo

root = tkinter.Tk()
root.title("テキストエリア")
root.geometry("400x200")

# ボタン用の関数
def btn():
    # my_text.insert("2.0", "文字を追加！") # 第一引数は文字列を指し、1.0の場合は「1行目の0文字目」という意味
    # my_text.insert(tkinter.END, "文字を追加！") # 入力されている時点の最後に入力される
    msg = my_text.get("1.0", tkinter.END)
    print(msg)

# 後で使うボタン
my_button = tkinter.Button(
    text="メッセージ", command=btn)
my_button.pack()

# 複数行のテキスト入力欄の作成
my_text = tkinter.Text()
my_text.pack()



# ウィンドウの表示
root.mainloop()
