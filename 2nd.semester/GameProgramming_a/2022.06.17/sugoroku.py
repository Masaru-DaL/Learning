GRID_COUNT = 30 # すごろくのマス目の数

# すごろくの盤面を表示する関数
def output_banmen():
  # マス数だけ・を出力して、最後にGoalと出力
  print("Start" + "・" * GRID_COUNT + "Goal")

# 盤面表示の関数を呼び出す
output_banmen()
