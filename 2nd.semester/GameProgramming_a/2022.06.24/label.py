import tkinter                  # tkinterモジュールのインポート
root = tkinter.Tk()             # ウィンドウオブジェクトを作る
root.title("ラベル表示")        # ウィンドウタイトルの設定
root.geometry("800x600")        # ウィンドウサイズの指定

my_label = tkinter.Label(
  root, text="表示する文字",
  font=("System", 36),
  fg = "pink", bg = "darkred"
  )
my_label.place(x=100, y=200)


root.mainloop()                 # ウィンドウの表示
