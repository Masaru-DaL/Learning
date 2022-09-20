from datetime import MAXYEAR
import tkinter
from tokenize import maybe                  # tkinterモジュールのインポート
# ウィンドウオブジェクトの作成～タイトルの指定
root = tkinter.Tk()
root.title("キャンバス表示")

# キャンバスを作成
my_canvas = tkinter.Canvas(
  root, width=400, height=600,
  bg = "skyblue",
)
# キャンバスを表示
my_canvas.pack()

# 画像を読み込み
my_image = tkinter.PhotoImage(
  file = "image/iroha.png"
)
# 画像を配置
my_canvas.create_image(
  2, 2,
  image = my_image,
  anchor = "nw"
)

# ウィンドウの表示
root.mainloop()
