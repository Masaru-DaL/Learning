import math

# 角度を15度ずつ変える
for theta in range(0, 361, 15):
    # ラジアンに変換する
    rad = 0
    # sin, cos, tanを出力
    print(f"{theta}度のsinは{0:.5f}, ", end="")
    print(f"cosは{0:.5f}, ", end="")
    print(f"tanは{0:.5f}です。")

