# 演習０（前回の復習）
#
# コマンドライン引数に文字をいくつか受け取り、
# 「その文字をすべて繋げたもの」と「その文字数」を
# 情報として出力するプログラムを作成してください。
import sys

in_str = ""
# for s in sys.argv:
#     in_str += s
for i, s in enumerate(sys.argv):
    if s != 0:
        in_str += s


print(f"{in_str}")
print(f"{len(in_str)}")
