# 演習１
# 資料のように、ウィンドウにラベルを２つ表示してみましょう。
# 位置は大体合っていればOKです。色やフォントは自由です。

# 発展演習（解説はなしの予定です）
# できた人は同様に、
# 「東」と「西」をウィンドウの良い位置に表示してみましょう。


# ウィンドウの作成
import tkinter
window = tkinter.Tk()

window.geometry("600x600")

window.maxsize(600, 600)


# 北ラベルの作成と配置
my_label1 = tkinter.Label(
  window, text="東",
  font = ("System", 36),
  fg = "black", bg = "white"
)
my_label2 = tkinter.Label(
  window, text="西",
  font = ("System", 36),
  fg = "black", bg = "white"
)
my_label3 = tkinter.Label(
  window, text="南",
  font = ("System", 36),
  fg = "black", bg = "white"
)
my_label4 = tkinter.Label(
  window, text="北",
  font = ("System", 36),
  fg = "black", bg = "white"
)

my_label1.place(x=550, y=275)
my_label2.place(x=0, y=275)
my_label3.place(x=275, y=550)
my_label4.place(x=275, y=0)

window.mainloop()
