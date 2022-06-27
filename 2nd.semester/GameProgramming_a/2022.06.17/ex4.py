# 演習４

# 新しいグループ名を決めたいと思います。
# LIST_MAE と LIST_USHIRO のそれぞれから単語をランダムで選び、
# つなげて「新しいグループ名は「xxx」に決まりました！」と出力してください。
# 何度も繰り返し実行して、いろんなグループ名ができることを確認しましょう。
import random

LIST_MAE = ["光", "少年", "キンキ", "セクシー", "スノー", "なにわ", "キング", "平成"]
LIST_USHIRO = ["ゲンジ", "隊", "キッズ", "ゾーン", "マン", "男子", "＆プリンス", "ジャンプ"]

result_first = random.choice(LIST_MAE)
result_back = random.choice(LIST_USHIRO)

print("新しいグループ名は" + result_first + result_back + "に決まりました！")
