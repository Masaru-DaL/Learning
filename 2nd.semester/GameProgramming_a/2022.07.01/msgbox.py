import tkinter
import tkinter.messagebox as messagebox

root = tkinter.Tk()
root.title("メッセージボックス")
root.geometry("400x200")

# ボタン用の関数
def btn_1():
    messagebox.showinfo("情報", "ボタンが押されました")
def btn_2():
    messagebox.showwarning("警告", "ボタンが押されました！")
def btn_3():
    messagebox.showerror("エラー", "ボタンが押されました！！！")
def btn_4():
    ret = messagebox.askyesno("はいいいえ", "ボタンが押されましたか？")
    print(ret)
def btn_5():
    ret = messagebox.askokcancel("OKキャンセル", "ボタンが押されましたがよろしいですか？")
    print(ret)


# ボタン１
button1 = tkinter.Button(bg="lightyellow",
    text="情報ボタン", width=50, height=2, command=btn_1)
# ボタン２
button2 = tkinter.Button(bg="pink",
    text="警告ボタン", width=50, height=2, command=btn_2)
# ボタン３
button3 = tkinter.Button(bg="red",
    text="エラーボタン", width=50, height=2, command=btn_3)
# ボタン４
button4 = tkinter.Button(bg="skyblue",
    text="はいいいえボタン", width=50, height=2, command=btn_4)
# ボタン５
button5 = tkinter.Button(bg="gold",
    text="OKキャンセルボタン", width=50, height=2, command=btn_5)

# 配置
button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()

# ウィンドウの表示
root.mainloop()
