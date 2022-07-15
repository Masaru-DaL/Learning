# 演習２
#
# 以下のプログラムを作成して下さい
# ・マウスの左ボタンが押されたら、押されている間大きくなる円をピンクで描画し、
#   離されたらそのサイズで赤の円で固定します
# ・マウスの右ボタンが押されたら、すでに描画した円を削除します
#
# メイン処理となる部分はすでに記述済みのため、
# マウスの関数の中、および、イベントとのバインドを記述して下さい
import tkinter
root = tkinter.Tk()                                 # ウィンドウの作成
root.title("円描画")                                # タイトルの設定

cvs = tkinter.Canvas(root, width=500, height=500)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

# マウスクリック位置の初期値は、存在しない値としておく
ms_x, ms_y = -1, -1
# マウスの左ボタンが押されているフラグ
ms_press_l = False
# マウスの右ボタンが押されてたフラグ
ms_press_r = False

# マウスのボタンが押された時に呼ばれる関数
def mouse_press(e):
    global ms_x, ms_y, ms_press_l, ms_press_r
    if e.num == 1:
        ms_x, ms_y = e.x, e.y
        ms_press_l = True

    elif e.num == 3:
        ms_press_r = True





# マウスのボタンが離された時に呼ばれる関数
def mouse_release(e):
    global ms_press_l, ms_press_r
    ms_press_l = False
    ms_press_r = False

# マウスのイベントとバインド
root.bind("<ButtonPress>", mouse_press)
root.bind("<ButtonRelease>", mouse_release)

# 円の半径
r = 0
# メイン処理
def mouse_main():
    global r

    # マウスの右ボタンが押された場合
    if ms_press_r == True:
        # 仮の円、固定の円ともに削除
        cvs.delete("KOTEI")
        cvs.delete("KARI")

    # マウスの左ボタンが押されている場合
    elif ms_press_l == True:
        # 半径を大きくする
        r += 1
        # 仮の円を削除
        cvs.delete("KARI")
        # ピンクで仮の円を描く
        cvs.create_oval(ms_x - r, ms_y - r, ms_x + r, ms_y + r,
                        outline="pink", width=2, tag="KARI")

    # マウスの左ボタンが離された場合（半径が０の場合を除く）
    elif r != 0:
        # 赤で固定の円を描く
        cvs.create_oval(ms_x - r, ms_y - r, ms_x + r, ms_y + r,
                    outline="red", width=2, tag="KOTEI")
        r = 0       # 半径を０にリセット

    root.after(20, mouse_main)

mouse_main()                                        # メイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
