class Runner:

  # コンストラクタ
  def __init__(self, name):
    self.name = name
    self.time = 0

  # 時間を記録する関数
  def record_time(self, time):
    self.time = time

  # 結果を出力する関数
  def output_time(self):
    if self.time == 0:
      print(f"{self.name}さんのタイムは記録されていません")
    else:
      print(f"{self.name}さんのタイムは{self.time}です")
