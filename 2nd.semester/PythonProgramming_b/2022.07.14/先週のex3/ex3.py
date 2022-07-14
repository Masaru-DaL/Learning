# 演習３
# 演習２の product.py をこのフォルダ（ex3）にコピーして下さい。
# 
# 以下の機能を Product クラスに加えて、
# 合わせてこちらのプログラムを修正して下さい。
# 
# 機能＜CUI化＞
# ・ユーザが「商品登録」「販売」「売上・個数出力」「売上・個数リセット」の
#   各操作を選べるようにする
# ・選んだ操作のうち「商品登録」「販売」は、ユーザが入力して実行できるようにする
# ・「売上・個数出力」「売上・個数リセット」は、メニューを選んだ時点で実行する
# プログラムの作り方は自由とします
#
# ※本プログラムの解答例は用意していないため、
#   なにか質問がある人は先生の方までお願いします。

# Productクラスをインポートする
from product import Product

product_list = []

while True:
    
    print("「１：商品登録」「２：販売」「３：売上・個数出力」「４：売上・個数リセット」「９：終了」")
    menu = int(input("行いたい機能を選んで下さい："))

    if menu == 1:
        # 登録
        name = input("登録する商品名を入力して下さい：")
        price = int(input("商品の価格を入力して下さい："))
        pro = Product(name, price)
        product_list.append(pro)
        
    elif menu == 2:
        # 販売
        for i in range(len(product_list)):
            print(f"「{i+1}:{product_list[i].name}({product_list[i].price}円)」", end=" ")
        print()
        sel = int(input("販売したい商品を上から選んで下さい："))
        pro = product_list[sel-1]
        pro.sell()
    
    elif menu == 3:
        # 売上・個数出力
        print(f"現在の総売上は {Product.total_sell}円、総販売個数は{Product.total_count}個です。")

    elif menu == 4:
        # 売上・個数リセット
        Product.total_sell = 0
        Product.total_count = 0
        print("総売上、総販売個数を０にしました")

    elif menu == 9:
        print("終了します。")
        break

