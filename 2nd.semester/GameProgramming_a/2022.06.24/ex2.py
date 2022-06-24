# 演習２
# １）現在「北」のボタンのみがあります。
# 　　同様に「南」のボタンを作って下さい。

# ２）「北」のボタンと「南」のボタンのどちらかが押されたら、
# 　　押された方の背景をピンクに、押されなかった方の背景を白にしてください。
# 　　「北」ボタンが押された時に背景がピンクになる処理は入っています
#　 　参考にして同様の処理を入れて下さい。

import tkinter

def click_n():
    button_n["bg"] = "pink"

# ウィンドウの作成
root = tkinter.Tk()
root.title("南北ボタン")
root.geometry("400x400")

# 北ボタンの作成と配置
button_n = tkinter.Button(
    root, text="北", font=("ＭＳ ゴシック", 24),
    fg="red", bg="white", command=click_n)
button_n.place(x=176, y=20)

# 南ボタンの作成と配置



# 画面の表示
root.mainloop()

