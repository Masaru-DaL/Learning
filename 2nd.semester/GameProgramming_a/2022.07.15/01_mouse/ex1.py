# 演習１
#
# ２回のクリックで、その２点を頂点とするような長方形を描画する
# プログラムを作成してください
#     配置してください。
# mouse_press 関数にコメント１）と２）が書いてあるので、
# そのコメントにそってプログラムを作成してください。
import tkinter
root = tkinter.Tk()                                 # ウィンドウの作成
root.title("長方形描画")                            # タイトルの設定

cvs = tkinter.Canvas(root, width=500, height=500)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

# 長方形の始点のx, y座標
start_x, start_y = 0, 0
# クリック数
click_count = 0

start_x, start_y, end_x, end_y = 0, 0, 0, 0
# マウスのボタンが押された時に呼ばれる関数
def mouse_press(e):
    global start_x, start_y, click_count, end_x, end_y

    # １）クリック数が０ならstart_x と start_y にx座標、y座標（e.x, e.y）を設定し、
    # クリック数を１にする
    if click_count == 0:
        start_x, start_y = e.x, e.y
        click_count = 1


    # ２）クリック数が０でなくて、
    # クリック数が１なら始点をstart_x, start_y、
    # 終点を今のx座標、y座標（e.x, e.y）として長方形を描画し、
    # クリック数を０にする
    elif click_count != 0 and click_count == 1:


        cvs.create_rectangle(start_x, start_y, e.x, e.y,
                        outline="blue", width=2)    # ※現在は、固定の位置に四角を描く処理なので修正する
        click_count = 0


root.bind("<ButtonPress>", mouse_press)             # マウスのボタンが押された時のイベントとバインド

# メイン処理
def mouse_main():
    # 特に処理はしない

    root.after(100, mouse_main)

mouse_main()                                        # メイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
