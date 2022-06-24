# tkinterモジュールをインポートする
import tkinter

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


root.mainloop()
