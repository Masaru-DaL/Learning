# 演習１
# 
# １）現在、ウィンドウにはボタンが２つあります。
#     このボタンの上の部分に１行のテキスト入力欄を２つ
#     配置してください。
# 
# ２）「上から下へ」ボタンが押されたら、
#     「下のテキスト入力欄」の文字を
#     「上のテキスト入力欄」の文字と同じにして下さい。
#     「下から上へ」ボタンは上下が逆で
#      同じ動きになるようにして下さい。
import tkinter

root = tkinter.Tk()
root.title("演習１")
root.geometry("400x200")

# ボタン用の関数
def btn1():
    # 上から下へボタン
    pass

def btn2():
    # 下から上へボタン
    pass

# 上から下へボタン
button1 = tkinter.Button(bg="white",
    text="上から下へ", width=20, height=2, command=btn1)
button1.place(x=10, y=120)
# 上から下へボタン
button2 = tkinter.Button(bg="pink",
    text="上から下へ", width=20, height=2, command=btn2)
button2.place(x=205, y=120)

# １行テキスト入力欄の作成（上）

# １行テキスト入力欄の作成（下）




# ウィンドウの表示
root.mainloop()
