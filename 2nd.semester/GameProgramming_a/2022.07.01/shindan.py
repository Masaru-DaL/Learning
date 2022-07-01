from cat_check import CAT_CHECK_LIST     # ネコ度チェックリスト
from cat_check import CAT_CHECK_RESULT   # ネコ度チェック結果
import tkinter

root = tkinter.Tk()
root.title("(=^・・^=)")
root.resizable(False, False)            # ウィンドウズのサイズ変更の抑制(サイズ変更不可)

# キャンバスの作成
canvas = tkinter.Canvas(
  root,
  width=800, height=600
)
canvas.pack()

back_image = tkinter.PhotoImage(file = "image/cat_background.png")

canvas.create_image(
  0, 0,
  image = back_image,
  anchor = "nw"
)


root.mainloop()
