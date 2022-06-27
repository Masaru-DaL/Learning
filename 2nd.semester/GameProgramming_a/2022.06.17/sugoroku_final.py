import random       # ランダムモジュールをインポートする

MASU_COUNT = 30     # すごろくのマス数を定数にしておく

# 盤面を表示する関数
# 引数：位置、表示する文字
def output_banmen(pos, ch):
    # 盤面の出力
    # 位置を表わす文字の左には「位置－１」個の・
    banmen = "・" * (pos - 1)
    banmen += ch
    # 位置を表わす文字の左には「マス数－位置」個の・
    banmen += "・" * (MASU_COUNT - pos)
    banmen += "Goal"
    print(banmen)

# プレイヤーの位置の変数
player_pos = 1
# CPUの位置の変数
cpu_pos = 1

# ずっとループする
while True:

    # 作った関数を「プレイヤーの位置」「プレイヤーの文字」を引数にして呼び出す
    output_banmen(player_pos, "Ｐ")
    # 作った関数を「CPUの位置」「CPUの文字」を引数にして呼び出す
    output_banmen(cpu_pos, "Ｃ")

    # 勝利判定を追加
    if player_pos == MASU_COUNT and cpu_pos == MASU_COUNT:
        print("同時にゴール！ 引き分けでした")
        continue
    elif player_pos == MASU_COUNT:
        print("プレイヤーがゴール！ プレイヤーの勝ち！！")
        break
    elif cpu_pos == MASU_COUNT:
        print("CPUがゴール！ CPUの勝ち！！")
        break

    # サイコロを振るメッセージを出力
    input("エンターキーでサイコロを振るよ！")
    # プレイヤー、CPUそれぞれのサイコロを振る
    p_dice = random.randint(1, 6)
    c_dice = random.randint(1, 6)
    # サイコロを振った結果を表示
    print(f"プレイヤーのダイスは{p_dice}、CPUのダイスは{c_dice}でした")
    # 振ったサイコロの目をそれぞれの位置に追加
    player_pos += p_dice
    cpu_pos += c_dice

    # 位置がゴールを行き過ぎていたら、ゴールの位置に修正
    if player_pos > MASU_COUNT:
        player_pos = MASU_COUNT
    if cpu_pos > MASU_COUNT:
        cpu_pos = MASU_COUNT
