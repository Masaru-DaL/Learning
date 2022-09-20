from credit_card import CreditCard

# ゴールドカードクラス
class GoldCard(CreditCard):

    CARD_NAME = "PIZZA_GOLD"

    # 割引率設定
    def set_discount(self, discount):
        self.discount = discount
        self.mag = (100 - self.discount) / 100

    # 購入
    def buy(self, item, price):
        price = int(price * self.mag)

        # スーパークラスを呼び出す
        super().buy(item, price)
