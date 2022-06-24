# おみくじゲーム：最終版
import tkinter                  # tkinterモジュールをインポートする
import random                   # ランダムモジュールをインポートする

# おみくじ結果リストを作成
OMIKUJI_KEKKA = ("大吉", "中吉", "吉", "末吉", "凶")

# 「おみくじを引く」ボタンを押されたときの処理
def click_omikuji():
    # おみくじ結果リストから、ランダムで結果を取得
    #kekka = random.choice(OMIKUJI_KEKKA)
    # kekka = OMIKUJI_KEKKA[random.randint(0, len(OMIKUJI_KEKKA))]
    ##kekka = OMIKUJI_KEKKA[random.randint(0, len(OMIKUJI_KEKKA) - 1)]
    #kekka = OMIKUJI_KEKKA[random.randint(1, len(OMIKUJI_KEKKA))]
    kekka = OMIKUJI_KEKKA[random.randint(1, len(OMIKUJI_KEKKA) - 1)]

    # ラベルに結果を設定
    kekka_label["text"] = kekka
    # ラベルを更新
    # ※この行は無くても、tkinterは一定間隔で情報が更新されるので大丈夫
    kekka_label.update()

root = tkinter.Tk()             # ウィンドウを作る
root.title("おみくじ")          # ウィンドウのタイトルを設定する
root.geometry("800x600")        # ウィンドウのサイズを設定する

# ウィンドウのサイズを変更不可にする（引数は横方向、縦方向）
root.resizable(False, False)
# 描画用のキャンバスを用意する
canvas = tkinter.Canvas(root, width=800, height=600)
canvas.pack()                   # キャンバスを配置する

# 画像データを用意する
back_image = tkinter.PhotoImage(file="image\miko.png")
# 画像データを配置する
canvas.create_image(0, 0, image=back_image, anchor="nw")
# ラベルの部品を作る（フォントは自由に指定可能）
kekka_label = tkinter.Label(root, text="結果",
    width=4, height=1, font=("", 120), fg="black", bg="white")
# ラベルを配置する
kekka_label.place(x=380, y=60)
# ボタンの部品を作る（フォントは自由に指定可能）
# ボタンが押されたときの処理を追加
omikuji_button = tkinter.Button(root, text="おみくじを引く",
    command=click_omikuji,
    width=15, height=1, font=("", 36), fg="blue", bg="white")
# ボタンを配置する
omikuji_button.place(x=360, y=400)

root.mainloop()              # ウィンドウを表示する（表示し続ける）
