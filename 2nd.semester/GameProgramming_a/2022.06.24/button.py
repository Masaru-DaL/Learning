import tkinter          # tkinterモジュールのインポート

def click_button():
  my_button["text"] = "押してしまいましたね..."


# ウィンドウオブジェクトの作成～サイズの指定
root = tkinter.Tk()
root.title("ボタン表示")
root.geometry("800x600")

# ボタンの作成
my_button = tkinter.Button(
  root, text = "押すなよ押すなよ！",
  font = ("Arial Black", 32),
  fg = "darkblue", bg = "lightblue",
  command=click_button
)

# ボタンの配置
my_button.place(x=350, y=300)

# ウィンドウの表示
root.mainloop()
