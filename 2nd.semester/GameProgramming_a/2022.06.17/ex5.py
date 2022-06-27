# 演習５

# ランダムに「１以上２未満」の小数を出力したいと思います。
# 文字のフォーマットを用いて、小数点以下２ケタまで表示してください。
# 何度も繰り返し実行して、いろんな数になることを確認しましょう。

import random

result = 1 + random.random()
print(f"{result:.2f}")

result1 = random.uniform(1,2)
# print(f"{result1:.2f}")
print(f"{result1:.2f}")

