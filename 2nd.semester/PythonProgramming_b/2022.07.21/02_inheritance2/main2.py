from credit_card import CreditCard
from gold_card import GoldCard

credit_card = GoldCard()

# 初期化
credit_card.clear_info()

# ゴールドカードの割引率を設定
credit_card.set_discount(5)

# 購入
credit_card.buy("プラモデル", 1500)
credit_card.buy("DVD", 4300)
credit_card.buy("食費", 500)

print("------")

# 購入リストを出力
credit_card.print_list()
