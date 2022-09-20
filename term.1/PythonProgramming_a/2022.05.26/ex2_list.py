# 関数
# 引数に数値（整数）を受け取り、
# １からその数までの、順番のリストを作成し、
# そのリストを戻り値にする

def make_list(num):

  local_list = [] # 空のリストを作成する
  for i in range(num): # 引数の数繰り返す
    local_list.append(i+1) # 空のリストに数を追加する

  return local_list # 作ったリストを戻り値にする

# print(make_list(20))
