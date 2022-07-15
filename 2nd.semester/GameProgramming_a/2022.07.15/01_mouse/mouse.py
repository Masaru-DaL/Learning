import tkinter          # tkinterのインポート

root = tkinter.Tk()                                 # ウィンドウの作成
root.title("mouse test")                            # タイトルの設定

cvs = tkinter.Canvas(root, width=500, height=500)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

# 変数
ms_x, ms_y, ms_press, ms_button = 0, 0, False, ""

# マウスが動いた時に呼ばれる関数
def mouse_move(e):
    global ms_x, ms_y
    ms_x, ms_y = e.x, e.y

# マウスのボタンが押された時に呼ばれる関数
def mouse_press(e):
    global ms_button, ms_press
    ms_press = True
    ms_button = e.num

# マウスのボタンが離された時に呼ばれる関数
def mouse_release(e):
    global ms_button, ms_press
    ms_press = False
    ms_button = ""

# マウスが動いた時のイベントとバインド
root.bind("<Motion>", mouse_move)
# マウスのボタンが押された時のイベントとバインド
root.bind("<ButtonPress>", mouse_press)
# マウスのボタンが離された時のイベントとバインド
root.bind("<ButtonRelease>", mouse_release)

# メイン処理
def mouse_main():

    m_font = ("Ariel", 30)
    m_text = f"位置：（{ms_x},{ms_y}）：{ms_press}({ms_button})"
    cvs.delete("MOUSE")
    cvs.create_text(250, 20, text=m_text, font=m_font,
                    fill="blue", tag="MOUSE")

    root.after(100, mouse_main)

mouse_main()                                        # メイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
