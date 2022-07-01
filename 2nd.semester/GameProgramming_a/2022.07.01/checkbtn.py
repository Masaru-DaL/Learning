import tkinter

root = tkinter.Tk()
root.title("チェックボタン")
root.geometry("400x200")

# チェックボタン用の関数
def chk():
    print("チェックボタンが押されました")
    c1 = cbool1.get()
    c2 = cbool2.get()
    print(f"{c1=},{c2=}\n")

# チェックボタン用の変数
cbool1 = tkinter.BooleanVar()
cbool2 = tkinter.BooleanVar()


# チェックボタンの作成
cbtn1 = tkinter.Checkbutton(
    text = "チェックボタン１",
    variable=cbool1,
    command=chk
)
cbtn1.pack()

cbtn2 = tkinter.Checkbutton(
    text = "チェックボタン２",
    variable=cbool2,
    command=chk
)
cbtn2.pack()





# ウィンドウの表示
root.mainloop()
