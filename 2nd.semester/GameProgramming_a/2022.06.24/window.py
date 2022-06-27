# tkinterモジュールのインポート
import tkinter
# ウィンドウオブジェクトを作る
root = tkinter.Tk()

# ウィンドウのタイトル指定
root.title('始めてのGUIで表示したウィンドウ')
# ウィンドウのサイズ指定
root.geometry('600x400')

# ウィンドウの最小サイズ(最小化は除く)の指定
root.minsize(300, 200)
# ウィンドウの最大サイズ(最大化した時を含む)の指定
root.maxsize(800, 600)

# ウィンドウオブジェクトの表示
root.mainloop()
