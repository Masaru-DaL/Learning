from mazemap import *               # 別ファイルから、マップ情報等すべてをインポート
import tkinter                      # tkinterのインポート
import tkinter.messagebox as messagebox     # メッセージボックスのインポート

maze_map = MAZE_MAP_1               # 迷路のマップをコピーする対象を選ぶ
my_pos = START_POS_1                # 自キャラの初期位置を一旦変数に入れる
my_x, my_y = my_pos                 # 自キャラの初期位置を設定

root  = tkinter.Tk()                # ウィンドウオブジェクトの作成
root.title("迷路塗りゲーム")        # ウィンドウタイトルの設定
root.geometry("800x560")        # ウィンドウタイトルの設定
root.resizable(False, False)        # ウィンドウのサイズ変更の抑制
# キャンバスの作成
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.place(x=0, y=0)                       # キャンバスの配置

# 画面に四角ブロックを表示する関数
# 引数はx方向の位置、y方向の位置、色
def put_block(x, y, color):
    # キャンバスに四角形を描画する（タグを指定）
    canvas.create_rectangle(x*80, y*80, x*80+79, y*80+79,
                            fill=color, width=0, tag="BLOCK")

nokori_count = 0                            # 残りのマス数（初期値は０）
# マップに合わせて、青ブロックを配置する
for y in range(7):                          # 行数分の繰り返し
    for x in range(10):                     # 列数分の繰り返し
        if maze_map[y][x] == 1:             # 該当マップ箇所のデータの取得
            put_block(x, y, "skyblue")      # ブロックを表示
        else:
            nokori_count += 1               # 残りのマス数を１加算

# 自キャラの画像ファイルを読み込み
my_img = tkinter.PhotoImage(file="../image/cat.png")
# 自キャラを画面に表示（タグを設定）
canvas.create_image(my_x*80, my_y*80, image=my_img,
                    anchor="nw", tag="MY")

key = ""                                    # キー入力値（初期値は空）
# キーが押された時の処理（押されたキーを保持）
def key_down(e):
    global key
    key = e.keysym
# キーが離された時の処理（押されたキーを破棄）
def key_up(e):
    global key
    key = ""

root.bind("<KeyPress>", key_down)           # キープレスと関数をバインド
root.bind("<KeyRelease>", key_up)           # キープリリースと関数をバインド

# メイン処理
def main_proc():
    # 各キーが押されている時に、その方向の行き先にブロックが無ければ
    # 自キャラの位置を移動させる
    global my_x, my_y, nokori_count         # 残りのマス数をglobal指定
    # 左シフトキーが押されたら、やり直すかのメッセージを出す
    if key == "Shift_L":
        ret = messagebox.askokcancel("やり直し", "ゲームを最初からやり直しますか？")
        # OKが押された場合
        if ret == True:
            canvas.delete("BLOCK")          # ブロックをすべて消す
            my_x, my_y = my_pos             # 自キャラの初期位置の設定を変数からに変更
            nokori_count = 0                # 残りマス数を一度０に
            # マップのマス分繰り返す
            for y in range(7):
                for x in range(10):
                    if maze_map[y][x] == 1:             # 該当箇所が壁だったら
                        put_block(x, y, "skyblue")      # ブロックを表示
                    if maze_map[y][x] == 2:             # 該当箇所が塗り済みだったら
                        maze_map[y][x] = 0              # 空白状態に戻す
                    if maze_map[y][x] == 0:             # 該当箇所が空白だったら
                        nokori_count += 1               # 残りのマス数を１加算

    if key == "Down" and maze_map[my_y+1][my_x] == 0:
        my_y += 1
    if key == "Up" and maze_map[my_y-1][my_x] == 0:
        my_y -= 1
    if key == "Right" and maze_map[my_y][my_x+1] == 0:
        my_x += 1
    if key == "Left" and maze_map[my_y][my_x-1] == 0:
        my_x -= 1
    # 自キャラの現在位置が空白なら
    if maze_map[my_y][my_x] == 0:
        maze_map[my_y][my_x] = 2            # マップの現在位置の数字を2にする
        put_block(my_x, my_y, "pink")       # ピンクのブロックを配置
        nokori_count -= 1                   # 残りのマス数を１減算

    # 自キャラを一度消去（タグを指定）
    canvas.delete("MY")
    # 自キャラの画像を表示（移動していた処理から変更）
    canvas.create_image(my_x*80, my_y*80, image=my_img,
                    anchor="nw", tag="MY")
    # 残りのマス数が０になったら
    if nokori_count == 0:
        canvas.update()                     # キャンバスを更新
        # メッセージボックスを表示
        messagebox.showinfo("おめでとう！", "すべての床を塗りました！")
    else:
        # 残りマスがある場合、一定間隔でメイン処理を繰り返す
        root.after(300, main_proc)

root.after(5000, main_proc)                                 # メイン処理の実行

root.mainloop()                     # ウィンドウの表示
