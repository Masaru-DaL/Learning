import random # ランダムモジュールをインポートする

GRID_COUNT = 30 # すごろくのマス目の数

# すごろくの盤面を表示する関数
# 引数: 位置、表示する文字
def output_field(pos, ch):
  # 位置を表す文字の左は「位置 - 1」個の・です
  field = "・" * (pos - 1)
  field += ch
  field += "・" *(GRID_COUNT - pos)
  field += "🏁\n"
  # マス数だけ・を出力して、スタートとゴールとして□と出力
  print(field)

# プレイヤーの位置の変数
player_pos = 1
# 対戦相手「CPU」の位置の変数
cpu_pos = 1

# ずっとループする
while True:
  # 盤面表示の関数を呼び出す
  output_field(player_pos, "👶")
  # CPUの盤面表示をする
  output_field(cpu_pos, "🦍")

  # サイコロを振るメッセージを出力
  input("エンターキーで'サイコロ'を振るよ！！")

  # プレイヤーとCPUのサイコロを振る
  player_dice = random.randint(1, 6)
  cpu_dice = random.randint(1, 6)

  # 勝利判定を追加
  if player_pos == GRID_COUNT and cpu_pos == GRID_COUNT:
    print("同時にゴール！引き分けです！")
    break
  elif player_pos == GRID_COUNT:
    print("おめでとう！プレイヤーの勝ちです！")
    break
  elif cpu_pos == GRID_COUNT:
    print("残念！CPUの勝ちです！")
    break

  # 転がしたダイス目を表示する
  print(f"プレイヤーのダイス目は[ {player_dice} ] 、CPUのダイス目は[ {cpu_dice} ]でした。")

  # 振ったサイコロの目を、それぞれの位置に追加
  player_pos += player_dice
  cpu_pos += cpu_dice

  if player_pos > GRID_COUNT:
    player_pos = GRID_COUNT
  if cpu_pos > GRID_COUNT:
    cpu_pos = GRID_COUNT
