# 演習２
# sportsman.py に親クラス「Sportsman」が、
# sumowrestler.py に子クラス「SumoWrestler」があります。
# まずは「SumoWrestler」クラスの処理を書いて下さい。
#
# その後、SportsmanクラスとSumoWrestlerクラスの
# インスタンスをいくつかずつ作って下さい。
# ※この場合、両方のインポートが必要なことに注意してください。
# 各インスタンスの「set_name()」「set_year()」メソッドを実行して、
# 名前と経験年数（SumoWrestlerクラスの場合は番付(ban)）を設定して下さい。
# その後、各インスタンスの「introduction()」メソッドを実行して下さい。

from sportsman import Sportsman
from sumowrestler import SumoWrestler

sumo1 = SumoWrestler()
sumo2 = SumoWrestler()
sumo3 = Sportsman()

sumo1.set_name("しまうま", "相撲部")
sumo2.set_name("らいおん", "横綱")
sumo3.set_name("きりん")

sumo1.set_year(2)
sumo2.set_year(40)
sumo3.set_year(30)

sumo1.introduction()
sumo2.introduction()
sumo3.introduction()
