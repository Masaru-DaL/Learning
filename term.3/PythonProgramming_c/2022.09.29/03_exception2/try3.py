# 関数
def double_num(num_str, index):
    n = int(num_str[index-1])
    return n ** 2


# 数字を２種類入力してもらう
print("入力した数字の指定番目の数を２乗します。")
nums = input("何桁かの数字を入力してください：")
index = input("何番目の数字かを指定してください：")

idx = int(index)
answer = double_num(nums, idx)
print(f"{nums}の{index}番目の数字を２乗すると{answer}です")



