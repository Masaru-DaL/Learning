# 演習２
# 
# １）現在、ウィンドウにはボタンと１行のテキスト入力欄があります。
#     このボタンの上の部分に複数行のテキスト入力欄を１つ
#     配置してください。
# 
# ２）入力文字数算出ボタンが押されたら、
#     複数行テキスト入力欄の文字数を数えて、
#     「入力文字数は５です」のように
#     １行テキスト欄に出力してください。（改行なども１文字に含めます）
#     出力の際、複数行テキスト入力欄の文字数から１減らして出力して下さい
#     ※複数行テキストの場合、最後に余計な１文字（記号）が付くようです
import tkinter

root = tkinter.Tk()
root.title("演習２")
root.geometry("400x400")

# ボタン用の関数
def btn1():
    # 入力文字数算出ボタン
    pass

# 入力文字数算出ボタン
# ※フォント３つ目の引数（あるいはキーワード引数の「weight」）に
#   "bold"を指定すると、太字にできます
button1 = tkinter.Button(bg="white", font=("", 16, "bold"),
    text="入力文字数を算出", width=25, height=2, command=btn1)
button1.place(x=10, y=320)

# １行テキスト入力欄の作成と配置
entry1 = tkinter.Entry(bg="skyblue",
    width=20, font=("Arial", 24))
entry1.place(x=10, y=250)

# 複数行テキスト入力欄の作成と配置


# ウィンドウの表示
root.mainloop()
