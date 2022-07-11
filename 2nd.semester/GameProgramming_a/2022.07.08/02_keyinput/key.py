import tkinter

# キー入力を検知したら、呼ばれる関数
# 引数として、押されたキーの情報が入って来ます
def key_down(e):
    # 押されたキーの情報から、キーの内容を取得
    key = e.keycode # 数字で表示される
    sym = e.keysym # 分かりやすく表示される
    print(f"{key}({sym})が押されました！")

root = tkinter.Tk()

# キーが押されたら、「key_down」関数を呼ぶように設定
root.bind("<KeyPress>", key_down)

root.mainloop()
