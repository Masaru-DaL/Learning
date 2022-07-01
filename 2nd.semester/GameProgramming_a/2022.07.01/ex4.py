# 演習４
# 
# １）ウィンドウにボタンがあります。
#     このボタンが押されたら、askyesno（はい/いいえメッセージボックス）を
#     WIN_MSG1のメッセージで表示して下さい。
#     「はい」が押されたら、終了関数「win_close」を呼び出して下さい。
#     「いいえ」が押された場合は処理をせず、メッセージボックスのみ閉じて下さい。

# ２）上記を発展させて、
#     最初のメッセージボックスで「はい」が押されたら、
#     WIN_MSG2のメッセージで次のメッセージボックスを表示して下さい。
#     そこで「はい」が押されたら、終了関数「win_close」を呼び出して下さい。
#     どちらのメッセージボックスでも「いいえ」が押された場合は処理をせず、
#     メッセージボックスのみ閉じて下さい。
import tkinter

WIN_MSG1 = "アプリを終了してもよろしいですか？"
WIN_MSG2 = "本当にアプリを終了してもよろしいですか？"

root = tkinter.Tk()
root.title("演習４")
root.geometry("400x200")

def win_close():
    # tkinterのウィンドウのクローズ
    root.quit()

# ボタン用の関数
def btn1():
    pass


# ボタン
button1 = tkinter.Button(bg="pink",
    text="アプリ終了", width=25, height=2, command=btn1)
button1.place(x=100, y=100)



# ウィンドウの表示
root.mainloop()
