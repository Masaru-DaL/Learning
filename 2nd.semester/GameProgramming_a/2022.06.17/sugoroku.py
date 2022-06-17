GRID_COUNT = 30 # すごろくのマス目の数

# すごろくの盤面を表示する関数
# 引数: 位置、表示する文字
def output_field(pos, ch):
  # 位置を表す文字の左は「位置 - 1」個の・です
  field = "・" * (pos - 1)
  field += ch
  field += "・" *(GRID_COUNT - pos)
  field += "🏁"
  # マス数だけ・を出力して、スタートとゴールとして□と出力
  print(field)

# プレイヤーの位置の変数
player_pos = 10
# 対戦相手「CPU」の位置の変数
cpu_pos = 9

# 盤面表示の関数を呼び出す
output_field(player_pos, "👶")

# CPUの盤面表示をする
output_field(cpu_pos, "🦍")
