from mazemap import MAZE_MAP_1      # 別ファイルから、マップ情報をインポート
import tkinter                      # tkinterのインポート
import tkinter.messagebox as messagebox     # メッセージボックスのインポート

maze_map = MAZE_MAP_1               # 迷路のマップをコピー

root  = tkinter.Tk()                # ウィンドウオブジェクトの作成
root.title("迷路塗りゲーム")        # ウィンドウタイトルの設定
root.geometry("800x560")        # ウィンドウタイトルの設定
root.resizable(False, False)        # ウィンドウのサイズ変更の抑制
# キャンバスの作成
canvas = tkinter.Canvas(width=800, height=560, bg="white")
canvas.place(x=0, y=0)                       # キャンバスの配置






root.mainloop()                     # ウィンドウの表示
