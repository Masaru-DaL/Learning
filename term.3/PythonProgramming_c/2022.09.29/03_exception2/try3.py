# 関数
def double_num(num_str, index):
    try:
        n = int(num_str[index - 1])
        return n**2
    except IndexError:
        print("IndexError: 指定したindexが無効です")
    except ValueError as e:
        print("ValueError: 指定した値は文字です")
        raise ValueError


# 数字を２種類入力してもらう
print("入力した数字の指定番目の数を２乗します。")
nums = input("何桁かの数字を入力してください：")
index = input("何番目の数字かを指定してください：")

try:
    idx = int(index)
    answer = double_num(nums, idx)
    print(f"{nums}の{index}番目の数字を２乗すると{answer}です")
except ValueError:
    print("ValueError: 数字を入力してください")
