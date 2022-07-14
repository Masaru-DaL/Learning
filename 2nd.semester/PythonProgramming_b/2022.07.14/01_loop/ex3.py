# 演習３
#
# 「英語での月」と「日本語の昔の月」が1月から順番に入っているリストがあります。
# zipを利用して、
# 「英語でJanuary、日本語で睦月です」
# というように12ヶ月全てを出力して下さい
EN_MONTHS = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]

JP_MONTHS = ["睦月", "如月", "弥生", "卯月", "皐月", "水無月",
            "文月", "葉月", "長月", "神無月", "霜月", "師走"]

count = 1
for english_month, japanese_month in zip(EN_MONTHS, JP_MONTHS):
  print(f"{count}月は、英語で「{english_month}」、日本語で「{japanese_month}」と読みます")
  count += 1
