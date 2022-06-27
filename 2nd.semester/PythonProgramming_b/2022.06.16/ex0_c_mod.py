# 演習０のｃのモジュール

# 引数の文字を逆にして返す
# 中身は理解しなくても大丈夫です
# ※余裕があったら解析してみて下さい（コメント省略）
def str_rev(str_in):
    str_out = ""
    list_s = []
    for s in str_in:
        list_s.append(s)

    print(list_s)
    for s in list_s:
        str_out = s + str_out
        
    return str_out
