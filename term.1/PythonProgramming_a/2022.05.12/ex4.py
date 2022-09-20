# 演習４
# ※プログラムを作成してください
#
# キー「英単語」と値「０または１」のペアである、辞書型のデータ「ENG_DIC」に対して、
# 値が０の場合は「(英単語)は動物です」、値が１の場合は「 (英単語)は植物です」と出力する。
# 出力例：
# dogは動物です
# bananaは植物です

# 英単語辞書
ENG_DIC = {'dolphin': 0, 'cherry': 1, 'bamboo': 1, 'violet': 1, 'wolf': 0, 'giraffe': 0, 'lotus': 1, 'gnu': 0, 'lion': 0, 'dandelion': 1}

for eng, kind in ENG_DIC.items():
  if kind == 0:
    print(str(eng) + ' は動物です\n')
  else:
    print(str(eng) + ' は植物です\n')

