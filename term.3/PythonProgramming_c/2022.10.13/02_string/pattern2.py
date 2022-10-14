import re

# 正規表現
print("正規表現[a.c]に一致するかチェックします。")
print(" . は任意の１文字を表します。")
ch = input("文字を入力してください：")

# 同じ条件を使う際などは、正規表現オブジェクトを作成（コンパイル）しておくことができる
ptn = None

# ※fullmatchを使うと完全一致になります
# match でのチェック（前方一致チェック）
res_match = None
# search でのチェック（部分一致チェック）
res_search = None

print(f"matchでのチェック結果：{res_match}")
print(f"searchでのチェック結果：{res_search}")

# オブジェクト.group()で情報として取得できる
if res_match != None:
    print(f"matchでの一致情報：{res_match.group()}")
if res_search != None:
    print(f"searchでの一致情報：{res_search.group()}")

# 正規表現パターンをコンパイル: compile()
# マッチオブジェクト
# 文字列の先頭がマッチするかチェック、抽出: match()
# 先頭に限らずマッチするかチェック、抽出: search()
# 文字列全体がマッチするかチェック: fullmatch()
# マッチする部分すべてをリストで取得: findall()
# マッチする部分すべてをイテレータで取得: finditer()
# マッチする部分を置換: sub(), subn()
# 正規表現パターンで文字列を分割: split()


