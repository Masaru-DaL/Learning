# tkinterモジュールをインポートする
import tkinter
import random # ランダムモジュールのインポート

# おみくじを引いた結果リストを作成
OMIKUJI_RESULT = ("大吉", "中吉", "吉", "末吉", "小吉", "100円")

# おみくじを引くボタンの処理
def click_omikuji():
  result = random.choice(OMIKUJI_RESULT)
  result_label["text"] = result
  result_label.update() # ラベルの更新(なくても一定間隔で更新される)

# windowの作成
root = tkinter.Tk()

root.title("おみくじ")
root.geometry("800x600")

# ウィンドウサイズ変更の可否(引数は横方向、縦方向)
root.resizable(False, False)

canvas = tkinter.Canvas(
  root, width=800, height=600
)
canvas.pack()

back_image = tkinter.PhotoImage(
  file = "image/miko.png"
)

canvas.create_image(
  0, 0,
  image = back_image,
  anchor = "nw"
)

# おみくじの結果を表示するラベルを用意する
result_label = tkinter.Label(
  root, text="結果",
  font = ("HGS行書体", 120),
  fg = "black", bg = "white",
  width=4, height=1
)
result_label.place(x=380, y=60)

# labelの背景の透明化の処理
# root.overrideredirect(True)
# root.lift()
# root.wm_attributes("-topmost", True)
# root.wm_attributes("-disabled", True)
# root.wm_attributes("-transparentcolor", "white")

# おみくじを引くボタンの作成
omikuji_button = tkinter.Button(
  root, text="おみくじを引く",
  font = ("HGS行書体", 36),
  fg = "blue", bg = "white",
  command=click_omikuji
)
omikuji_button.place(x=360, y=400)


root.mainloop()
