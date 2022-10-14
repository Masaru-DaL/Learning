

num = float(input("数字を入力してください："))

# 【abs】絶対値（組み込み関数）
print(f"{num}の絶対値は「{0}」です。")
# 【math.fabs】絶対値（math）
print(f"{num}の絶対値は「{0}」です。")
# 【math.sqrt】平方根を求める
if num >= 0:
    print(f"{num}の平方根は「{0}」です。")
# 【math.floor】切り捨てを求める
print(f"{num}を切り捨てると「{0}」です。")
# 【math.ceil】切り上げを求める
print(f"{num}を切り上げると「{0}」です。")
# 【math.trunc】整数部分を求める
print(f"{num}の整数部分は「{0}」です。")
# 【math.pi】円周率
print(f"円周率は「{0}」です。")
# 【math.e】ネイピア数（自然対数の底）
print(f"ネイピア数は「{0}」です。")
# 【math.log】自然対数
print(f"log({num})は「{0}」です。")
# 【math.log】常用対数
print(f"log10({num})は「{0}」です。")


