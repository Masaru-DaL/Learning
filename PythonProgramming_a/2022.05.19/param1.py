# 引数の値の確認
def test_param(num_p, str_p, list_p):
    print("2nd:", num_p, str_p, list_p)
    num_p, str_p, list_p = 2, "b", [4,5]
    print("3rd:", num_p, str_p, list_p)

num1, str1, list1 = 1, "a", [1, 2, 3]
print("1st:", num1, str1, list1)
test_param(num1, str1, list1)
print("4th:", num1, str1, list1)
