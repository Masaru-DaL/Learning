from mazemap import *      # 別ファイルから、マップ情報をインポート
import tkinter                      # tkinterのインポート
import tkinter.messagebox as messagebox     # メッセージボックスのインポート

maze_map = MAZE_MAP_5               # 迷路のマップをコピー
my_pos = START_POS_5                # 自キャラの初期位置を一旦変数に入れる
my_x, my_y = my_pos

root  = tkinter.Tk()                # ウィンドウオブジェクトの作成
root.title("迷路塗りゲーム")        # ウィンドウタイトルの設定
root.geometry("800x560")        # ウィンドウタイトルの設定
root.resizable(False, False)        # ウィンドウのサイズ変更の抑制
# キャンバスの作成
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.place(x=0, y=0)                       # キャンバスの配置

# 画面に四角ブロックを描画する
def put_block(x, y, color):
  # キャンバスに四角形を描画する(タグを指定)
  canvas.create_rectangle(
    x*80, y*80, x*80+79, y*80+79, # 80*80の四角にすると隙間が空かなくなるため、79*79にする。(スタート位置は80にする)
    fill=color, width=0, tag="BLOCK"
  )

nokori_count = 0
# マップに合わせて青ブロックを表示
for y in range(7):              # 行数分の繰り返し
  for x in range(10):           # 列数分の繰り返し
    if maze_map[y][x] == 1:
      put_block(x, y, "skyblue")
    else:
      nokori_count += 1

# ここでは設定しなくする
# my_x, my_y = 1, 1         # 自キャラの初期位置

my_img = tkinter.PhotoImage(file="../image/cat.png")

canvas.create_image(
  my_x*80, my_y*80,
  image=my_img,
  anchor="nw",
  tag="MY"
)

key = ""                      # キー入力値
# キーが押された時の処理(押されたキーを保持)
def key_down(e):
  global key
  key = e.keysym
# キーが離された時の処理(押されたキーを破棄)
def key_up(e):
  global key
  key = ""

root.bind("<KeyPress>", key_down)       # キープレスと関数をバインド
root.bind("<KeyRelease>", key_up)       # キーリリースと関数をバインド

# メイン処理
def main_proc():
  global my_x, my_y, nokori_count, key
  # 左シフトキーが押されたら、やり直すかのメッセージを出す
  if key == "Shift_L":
    ret = messagebox.askokcancel("やり直し", "ゲームを最初からやり直しますか？")
    key = ""
    if ret == True:             # OKが押された場合
      canvas.delete("BLOCK")
      my_x, my_y = my_pos
      nokori_count = 0
      for y in range(7):
        for x in range(10):
          if maze_map[y][x] == 1:
            put_block(x, y, "skyblue")
          if maze_map[y][x] == 2:
            maze_map[y][x] = 0
          if maze_map[y][x] == 0:
            nokori_count += 1



  # キーが押されているときに、その方向の行き先にブロックがなければ自キャラの位置を移動させる
  if key == "Down" and maze_map[my_y+1][my_x] == 0:
    my_y += 1
  if key == "Up" and maze_map[my_y-1][my_x] == 0:
    my_y -= 1
  if key == "Right" and maze_map[my_y][my_x+1] == 0:
    my_x += 1
  if key == "Left" and maze_map[my_y][my_x-1] == 0:
    my_x -= 1

  # 自キャラの位置が空白なら
  if maze_map[my_y][my_x] == 0:
    maze_map[my_y][my_x] = 2              # マップの現在位置を2にする
    put_block(my_x, my_y, "pink")         # ピンクのブロックを配置
    nokori_count -= 1

  # 自キャラを一度消去
  canvas.delete("MY")
  # 自キャラの表示位置を移動
  canvas.create_image(
  my_x*80, my_y*80,
  image=my_img,
  anchor="nw",
  tag="MY"
  )

  if nokori_count == 0:
        canvas.update()                     # ３２）キャンバスを更新
        # ３３）メッセージボックスを表示
        messagebox.showinfo("おめでとう！", "すべての床を塗りました！")
  else:
        # ３４）残りマスがある場合、一定間隔でメイン処理を繰り返す
        root.after(300, main_proc)

main_proc()                         # 最初にメイン処理を呼び出す
root.mainloop()                     # ウィンドウの表示
