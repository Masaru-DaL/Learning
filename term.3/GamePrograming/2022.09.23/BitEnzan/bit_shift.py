
num1 = 35
print(f"{num1} (２進数:{num1:b})")

print("左に２ビットシフト")
num2 = num1 << 2
print(f"{num2} (２進数:{num2:b})")

print("右に１ビットシフト")
num3 = num1 >> 1
print(f"{num3} (２進数:{num3:b})")

# ===== 以下は計算結果例 =====
num1 = 35 # (２進数:100011＝35)
num2 = num1 << 2 # (２進数:10001100＝140)
num3 = num1 >> 1 # (２進数:10001＝17)

num1 = -35 # (２進数:-100011＝-35)
num2 = num1 << 2 # (２進数:-10001100＝-140)
num3 = num1 >> 1 # (２進数:-10001＝-18)
