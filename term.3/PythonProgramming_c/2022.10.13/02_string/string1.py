# 文字列関連

# 【row文字列】先頭に r(R)を書くと、/がエスケープシーケンスされずにそのまま扱われる。
print("あ\tい\\う\'え\nお")


# 文字列のチェック
ch = input("文字を入力してください：")

# 【isalpha】文字の場合True（日本語も調べられる模様）
print(f"{ch}のisaphaの結果は{0}です")
# 【isnumeric】数を表す文字の場合True（壱などもTrueになる模様…int型に変換できないのに）
print(f"{ch}のisnumericの結果は{0}です")
# 【isalnum】数字か文字の場合True
print(f"{ch}のisalnumの結果は{0}です")
# 【isdecimal】10進数の数字を表す場合True
print(f"{ch}のisdecimalの結果は{0}です")
# 【isdigit】数字の文字の場合True（上との差は微妙）
print(f"{ch}のisdigitの結果は{0}です")

