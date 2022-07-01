# 演習３
# 
# １）現在、ウィンドウにはボタンとテキストボックスがあります。
#     このボタンの上の部分に２つのチェックボタンを配置してください。
# 
# ２）チェック状態検出ボタンが押されたら、
#     １行テキスト入力欄にチェックされている方の
#     チェックボタンの名前を表示してください。
#     両方チェックされているなら「両方」
#     どちらもチェックされていないなら「チェックなし」と表示してください。
import tkinter

root = tkinter.Tk()
root.title("演習３")
root.geometry("400x400")

# ボタン用の関数
def btn1():
    # チェック状態検出ボタン
    pass

# チェック状態検出ボタン
# ※フォント３つ目の引数（あるいはキーワード引数の「weight」）に
#   "bold"を指定すると、太字にできます
button1 = tkinter.Button(bg="white", font=("", 16, "bold"),
    text="チェック状態を検出", width=25, height=2, command=btn1)
button1.place(x=10, y=320)

# １行テキスト入力欄の作成と配置
entry1 = tkinter.Entry(bg="skyblue",
    width=20, font=("Arial", 24))
entry1.place(x=10, y=250)

# チェックボタン用の変数

# チェックボタン２つの作成と配置


# ウィンドウの表示
root.mainloop()
