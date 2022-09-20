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

# ねこフィールドの作成
neko_field = []
# チェックフィールドの作成
check_field = []
for y in range(10):
    neko_field.append([0,0,0,0,0,0,0,0])
    check_field.append([0,0,0,0,0,0,0,0])

# 並びチェック関数
def check_neko():
    for y in range(10):
        for x in range(8):
            check_field[y][x] = neko_field[y][x]

    # 横の並びをチェック（内側の６列のみ）
    for y in range(10):
        for x in range(1, 7):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合で
            # 左右ともに同じねこの場合
            if ch > 0 \
               and check_field[y][x-1] == ch \
               and check_field[y][x+1] == ch:
                # ３マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y][x-1] = 7
                neko_field[y][x+1] = 7
    # 縦の並びをチェック（一番下と一番上以外）
    for y in range(1, 9):
        for x in range(8):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合で
            # 上下ともに同じねこの場合
            if ch > 0 \
               and check_field[y-1][x] == ch \
               and check_field[y+1][x] == ch:
                # ３マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y-1][x] = 7
                neko_field[y+1][x] = 7
    # 斜めの並びをチェック（一番外枠以外）
    for y in range(1, 9):
        for x in range(1, 7):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合
            if ch > 0:
                # 左上と右下がともに同じねこの場合
                if check_field[y-1][x-1] == ch \
                   and check_field[y+1][x+1] == ch:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x-1] = 7
                    neko_field[y+1][x+1] = 7
                # 右上と左下がともに同じねこの場合
                if check_field[y-1][x+1] == ch \
                   and check_field[y+1][x-1] == ch:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x+1] = 7
                    neko_field[y+1][x-1] = 7


# ねこ描画関数
def draw_neko():
    # ねこを消去 ※ゲームメイン処理から移動
    cvs.delete("NEKO")

    for y in range(10):
        for x in range(8):
            img_no = neko_field[y][x]       # 画像の番号を取得
            if img_no > 0:                  # 画像の番号が１以上の場合
                # その番号のねこ画像を描画
                cvs.create_image(
                    x*72+24, y*72+24,
                    image=neko_images[img_no], anchor="nw", tag="NEKO"
                )

# ねこ落下関数
def fall_neko():
    is_fall = False     # 落下ありフラグを追加
    # ２次元リスト的な繰り返しをするが、
    # 縦方向は下から順に処理を行う
    for y in range(8, -1, -1):
        for x in range(8):
            # その位置が空でなく、１つ下が空の場合
            if neko_field[y][x] != 0 and neko_field[y+1][x] == 0:
                # １つ下の位置にこの位置のねこを設定する
                neko_field[y+1][x] =  neko_field[y][x]
                # この位置を空にする
                neko_field[y][x] = 0
                # 落下ありフラグをTrueに
                is_fall = True
    # 落下ありフラグを戻り値にする
    return is_fall

# ねこ消去関数（戻り値：消したねこの数）
def sweep_neko():
    swe = 0         # 消したねこの数
    for y in range(10):
        for x in range(8):
            if neko_field[y][x] == 7:       # その場所が肉球の場合
                neko_field[y][x] = 0        # 空にする
                swe += 1                    # 消した数を１増加
    return swe                              # 消した数を戻り値にする

# ねこを最上段の行に追加する関数
def add_neko():
    # 最上段のマスそれぞれに、ねこ（空白の場合あり）を追加
    for x in range(8):
        neko_field[0][x] = random.randint(0, 6)

# ゲームオーバーチェック関数（戻り値：True ゲームオーバー）
# ※この関数は、ねこを消しきったあとに呼ぶ必要があります
def check_gameover():
    for x in range(8):
        # 一番上の列をチェック
        if neko_field[0][x] > 0:            # その場所にねこがある場合
            return True                     # ゲームオーバー
    return False                            # 無ければ、ゲームオーバーじゃない


cvs = tkinter.Canvas(root, width=912, height=768)   # キャンバスの作成
cvs.pack()                                          # キャンバスの配置

bg = tkinter.PhotoImage(file="../image/neko_bg.png")            # 背景画像
cursor = tkinter.PhotoImage(file="../image/neko_cursor.png")    # カーソル画像

cvs.create_image(456, 384, image=bg)                # 背景画像の表示

# マウスのx座標、y座標、クリックフラグの変数
ms_x, ms_y, ms_click = 0, 0, False

# マウスが動いた時に呼ばれる関数
def mouse_move(e):
    global ms_x, ms_y
    ms_x, ms_y = e.x, e.y                           # イベントのマウス位置を保持

# マウスのボタンが押された時に呼ばれる関数
def mouse_press(e):
    global ms_click
    ms_click = True                                 # クリックフラグをTrueにする

root.bind("<Motion>", mouse_move)                   # マウスが動いた時のイベントとバインド
root.bind("<ButtonPress>", mouse_press)             # マウスのボタンが押された時のイベントとバインド

step = 0                # ゲームの処理を分ける変数
score = 0               # スコア
chain = 1               # 連鎖数（消して、落ちて、また消える…という回数
next_neko = 0           # 次のねこ
go_timer = 0            # ゲームオーバー用のタイマー

# ゲームメイン処理
def game_main():
    # マウス関係の変数をglobalに
    # グローバル変数指定にnext_nekoを追加
    global ms_x, ms_y, ms_click, step, score, chain, next_neko
    global go_timer
    # 初期状態：タイトル画面を表示
    if step == 0:
        # ゲームタイトルを表示
        t_font = ("Areal", 102, "bold")
        cvs.create_text(312, 240, text="ねこねこ", fill="violet",
                        font=t_font, tag="TITLE")
        # メッセージを表示
        m_font = ("Areal", 50, "bold")
        cvs.create_text(312, 560, text="Click to start.", fill="orange",
                        font=m_font, tag="TITLE")
        step = 1        # クリック待ちへ

    # スタート待ち
    elif step == 1:
        # クリックされたら
        if ms_click == True:
            # ねこフィールドをクリア
            for y in range(10):
                for x in range(8):
                    neko_field[y][x] = 0
            ms_click = False    # クリックフラグをFalseに
            score = 0           # スコアを０に
            chain = 1           # 連鎖数を１に
            next_neko = 0       # 次のねこをクリアしておく
            go_timer = 0        # ゲームオーバー用タイマーに０をセット
            cvs.delete("TITLE") # タイトル画面の情報を消去
            add_neko()          # 最上段にねこを配置
            draw_neko()         # ねこを描画
            step = 2            # 落下処理へ

    # 落下処理
    elif step == 2:
        # ねこを落下、落下したものが無ければ
        if fall_neko() == False:
            step = 3            # チェックへ
        draw_neko()             # ねこ描画

    # チェック処理
    elif step == 3:
        # ねこの並びをチェック
        check_neko()
        draw_neko()             # ねこ描画
        step = 4                # 消去処理へ

    # 消去処理
    elif step == 4:
        sw = sweep_neko()           # ねこ消去関数を実行
        score += sw * chain * 10    # スコアに、「消した数✕連鎖数✕10」を加算
        # １つ以上消している場合
        if sw > 0:
            chain += 1              # 連鎖数を１増加
            step = 2                # 落下処理へ
        else:
            # 消してない場合で、ゲームオーバーじゃない場合
            if check_gameover() == False:
                # 次のねこをセット
                next_neko = random.randint(1, 6)
                step = 5            # マウス入力へ
            else:
                step = 6            # ゲームオーバーへ

            ms_click = False        # 先行入力されているクリックを削除する

    # マウス入力
    elif step == 5:
        # マウスの位置が盤面上の場合
        # ※数値は、画像に合わせて計算済みの値となっています
        if 24 <= ms_x < 24+72*8 and 24 <= ms_y < 24+72*10:
            # カーソル位置を計算
            cursor_x = int((ms_x-24)/72)
            cursor_y = int((ms_y-24)/72)
            # マウスがクリックされている場合
            if ms_click == True:
                # 最上段にねこを配置
                add_neko()
                # 次のねこを、カーソル位置にセット
                neko_field[cursor_y][cursor_x] = next_neko
                # 次のねこをクリア
                next_neko = 0
                ms_click = False                    # マウスクリックフラグをFalseにする
                chain = 1                           # 連鎖数を１に
                step = 2                            # 落下処理へ
        else:
            # 盤面外の場合、cursor_xを－１にする
            cursor_x = -1

        # カーソルを消去
        cvs.delete("CURSOR")
        # カーソルが盤面内の場合
        if cursor_x != -1:
            # カーソルを表示
            cvs.create_image(
                cursor_x*72+24, cursor_y*72+24,
                image=cursor, anchor="nw", tag="CURSOR"
            )
        draw_neko()             # ねこ描画
    # ゲームオーバー
    elif step == 6:
        # ゲームオーバー用タイマーが０の場合
        if go_timer == 0:
            # ゲームオーバーの文字を表示
            g_font = ("Areal", 60, "bold")
            cvs.create_text(312, 348, text="GAME OVER", fill="red",
                            font=g_font, tag="GAMEOVER")
        # ゲームオーバー用タイマーを１増加
        go_timer += 1
        # ゲームオーバー用タイマーが50になった場合
        if go_timer == 50:
            cvs.delete("GAMEOVER")      # ゲームオーバーの文字を消去
            step = 0                    # タイトル画面へ

    # 画面情報を削除
    cvs.delete("INFO")
    # スコアを描画
    s_font = ("Areal", 32, "bold")
    cvs.create_text(160, 60, text=f"SCORE {score}", fill="blue",
                    font=s_font, tag="INFO")
    # 次のねこを、次のねこ位置に表示
    if next_neko > 0:
        cvs.create_image(752, 128, image=neko_images[next_neko],
                         tag="INFO")

    root.after(100, game_main)                      # ゲームメイン処理を繰り返す

game_main()                                         # ゲームメイン処理の呼び出し
root.mainloop()                                     # ウィンドウの表示
