# 演習２－ａ
# product.py に Productクラスを作成してください。
# （内容はproduct.pyに記載してあります）
#
# Productクラスを利用して、以下を行って下さい。
# ※ユーザからの入力などは必要なく、プログラム上に記載してください。
# ・商品とその金額の登録（複数種類の登録）
# ・商品の販売（商品ごとに何度か行う）
# ・クラス変数の「total_sell」を用いて、総売上の出力
#
# 演習２－ｂ
# 以下の機能をクラスおよび本プログラムに追加してください
# ＜売上個数管理＞
# ・クラス変数に「個数」を追加。初期値は0
# ・１個売れるごとに「個数」を１加算
# ・総売上を出力する際に、総販売個数も出力

# Productクラスをインポートする
from product import Product
# 商品の登録
cake = Product("ケーキ", 500)
dango = Product("だんご", 180)
senbei = Product("せんべい", 50)
# 商品の販売
cake.sell()
dango.sell()
senbei.sell()
# 総売上の出力
print(f"総売り上げ個数は{Product.total_num}個で、総売り上げ金額は{Product.total_sell}円です")
