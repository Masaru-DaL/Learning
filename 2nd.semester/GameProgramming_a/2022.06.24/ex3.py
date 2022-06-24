# 演習３
# １）ウィンドウにキャンバスを用意し、
# 　　imageフォルダにある「yse1.png」～「yse4.png」を表示してください
# 　　どの位置にどの画像を配置しても構いません。
# 　　まずは重ならない程度に位置を調整しましょう。

# ２）４つの画像の位置を、ウィンドウの４隅になるように調整してください。
# 　　どの位置にどの画像を配置しても構いません。
# 　　画像の位置を微妙に調整していってもOKですが、４隅の座標は分かるので、
# 　　「nw」の左上は「北西」という意味から、
# 　　anchor の指定を類推できると楽かもしれません。
# 　　（あるいはanchorの指定方法をインターネットなどで調べてみて下さい）

import tkinter

root = tkinter.Tk()
root.title("キャンパス案内")

WIDTH_SIZE = 600
HEIGHT_SIZE = 600

my_canvas = tkinter.Canvas(
  root, width=WIDTH_SIZE, height=HEIGHT_SIZE,
  bg = "blue"
)
my_canvas.pack()

image1 = tkinter.PhotoImage(
  file = "image/yse1.png"
)
image2 = tkinter.PhotoImage(
  file = "image/yse2.png"
)
image3 = tkinter.PhotoImage(
  file = "image/yse3.png"
)
image4 = tkinter.PhotoImage(
  file = "image/yse4.png"
)

my_canvas.create_image(
  400, 400,
  image = image1,
  anchor = "nw"
)
my_canvas.create_image(
  400, 400,
  image = image2,
  anchor = "se"
)
my_canvas.create_image(
  520,2,
  image = image3,
  anchor = "nw"
)
my_canvas.create_image(
  500,550,
  image = image4,
  anchor = "nw"
)


root.mainloop()
