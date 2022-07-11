import tkinter

# 入力キー
key = ""
# キーが押された時の関数
def key_down(e):
    # 押されたキーの情報から、キーの内容を取得
    global key
    key = e.keysym
# キーが離された時の関数
def key_up(e):
    # 押されたキーの情報から、キーの内容を取得
    global key
    key = ""

c_pos = [400, 300]  # キャラクターの初期位置
MOVE = 10           # １回ごとにキャラが動く距離
INTERVAL = 10      # chara_move が呼ばれる間隔

def chara_move():
    # 押されたキーの方向に、キャラの位置を移動
    if key == "Right":
        c_pos[0] += MOVE
    if key == "Left":
        c_pos[0] -= MOVE
    if key == "Down":
        c_pos[1] += MOVE
    if key == "Up":
        c_pos[1] -= MOVE
    # 指定の位置に、指定のタグの画像を移動
    canvas.coords("CAT", c_pos[0], c_pos[1])
    # 一定間隔後に再度この関数を実行
    root.after(INTERVAL, chara_move)

root = tkinter.Tk()
root.title("風船旅行")
# キャンバスの作成と配置
canvas = tkinter.Canvas(width=800, height=600, bg="white")
canvas.pack()
# 背景画像ファイルを読み込み
bg_img = tkinter.PhotoImage(file="../image/sky.png")
# 背景画像を表示（タグを設定）
canvas.create_image(0, 0, image=bg_img, anchor="nw")

# キャラ画像ファイルを読み込み
cat_img = tkinter.PhotoImage(file="../image/baloon.png")
# キャラ画像を表示（タグを設定）
canvas.create_image(c_pos[0], c_pos[1], image=cat_img,
                    tag="CAT")

# キーが押された時、離された時の処理をバインド
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)

# キャラクター移動処理
chara_move()

root.mainloop()
