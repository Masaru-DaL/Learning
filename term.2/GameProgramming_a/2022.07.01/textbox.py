import tkinter

root = tkinter.Tk()
root.title("テキストボックス")
root.geometry("400x200")

# ボタン用の関数
def btn():
    # my_entry2.insert(5, "ボタンが押されました")
    # my_entry2.delete(1, 3)
    # my_entry2.delete(0, tkinter.END)
    my_button["text"] = my_entry2.get() # テキストボックスに入力した文字がボタン上に表示される

# 後で使うボタン
my_button = tkinter.Button(
    text="ボタン", width=50, height=2, command=btn,
    bg="lightyellow")
my_button.place(x=10, y=120)

# １行のテキスト入力欄の作成
my_entry1 = tkinter.Entry(width=20)
my_entry1.place(x=10, y=10)


my_entry2 = tkinter.Entry(
    width=20, font=("Arial", 24),
    bg="darkblue", fg="skyblue"
)
my_entry2.place(x=10, y=50)


# ウィンドウの表示
root.mainloop()
