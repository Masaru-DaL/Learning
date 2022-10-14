# 文字列関連

# 文字列のチェック
#ch = input("文字を入力してください：")
ch = "cdnhYPajSlDaACae"

# 【upper】大文字に置換
print(f"{ch}をすべて大文字にすると{ch}です")
# 【lower】小文字に置換
print(f"{ch}をすべて小文字にすると{ch}です")
# 【strip】指定文字（指定しない場合は空白や改行）を先頭・末尾から削除
rm_str = "abcdeABCDE"
print(f"{ch}の先頭・末尾から{rm_str}をすべて取り除くと{ch}です")
# 【zfill】指定桁数で左0埋めする
print(f"{ch}を左0埋めして20桁にすると{ch}です")
# 【find】指定文字が最初に出現する位置を返す
print(f"{ch}の中で、「a」が出てくるのは{ch}番目です")
# 【replace】指定文字を別の文字で置き換える
print(f"{ch}の「a」を「Z」に置き換えると{ch}です")
# 【count】指定文字の数を数える
print(f"{ch}にある「a」の数は{ch}個です")
# 【in】指定文字があるかチェックする（リストと同様）
print(f"{ch}に「a」があるかのチェック結果は{ch}です")



