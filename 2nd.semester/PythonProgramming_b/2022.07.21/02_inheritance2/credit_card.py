# クレジットカードクラス
class CreditCard:
    
    CARD_NAME = "PIZZA"
    
    # 情報初期化
    def clear_info(self):
        self.items = []
        self.prices = []
        
    # 購入
    def buy(self, item, price):
        print(f"{price}円の商品、{item}を購入しました。")
        self.prices.append(price)
        self.items.append(item)
        
    # 購入一覧＋合計金額出力
    def print_list(self):
        total = 0
        for item, price in zip(self.items, self.prices):
            print(f"{item}（{price}円）")
            total += price
        print(f"購入合計金額は{total}円です")
