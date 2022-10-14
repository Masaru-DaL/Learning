

# 正規表現
print("正規表現[a.c]に一致するかチェックします。")
print(" . は任意の１文字を表します。")
ch = input("文字を入力してください：")

# [.]
# match でのチェック（前方一致チェック）
res_match = None
# search でのチェック（部分一致チェック）
res_search = None

print(f"matchでのチェック結果：{res_match}")
print(f"searchでのチェック結果：{res_search}")


