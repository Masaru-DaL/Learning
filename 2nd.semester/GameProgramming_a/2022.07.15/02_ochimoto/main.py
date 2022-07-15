import tkinter          # tkinterのインポート
import random           # randomのインポート

root = tkinter.Tk()                                 # ウィンドウの作成
root.title("落ち物パズル「ねこねこ」")              # タイトルの設定
root.resizable(False, False)                        # 画面のリサイズの抑制

# 猫ブロック画像リスト（最初の１つ目は空にしておく）
neko_images = [
    None,
    tkinter.PhotoImage(file="../image/neko1.png"),
    tkinter.PhotoImage(file="../image/neko2.png"),
    tkinter.PhotoImage(file="../image/neko3.png"),
    tkinter.PhotoImage(file="../image/neko4.png"),
    tkinter.PhotoImage(file="../image/neko5.png"),
    tkinter.PhotoImage(file="../image/neko6.png"),
    tkinter.PhotoImage(file="../image/neko_niku.png")
]

cvs = tkinter.Canvas(root, width=912, height=768)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

bg = tkinter.PhotoImage(file="../image/neko_bg.png")            # 背景画像
cursor = tkinter.PhotoImage(file="../image/neko_cursor.png")    # カーソル画像

cvs.create_image(456, 384, image=bg)                # 背景画像の表示

# ゲームメイン処理
def game_main():

    # ※数値は、画像に合わせて計算済みの値となっています
    #if 24 <= ms_x < 24+72*8 and 24 <= ms_y < 24+72*10:
        # カーソル位置を計算
        #cursor_x = int((ms_x-24)/72)
        #cursor_y = int((ms_y-24)/72)

    root.after(100, game_main)                      # ゲームメイン処理を繰り返す

game_main()                                         # ゲームメイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
