
MONTHS = 12
# 間に何も開けない
print('１年は', end = '')

# printの途中は何も開けない
# printの最後はスペースを開ける
for i in range(MONTHS):
    print(i+1, '月', sep = '', end = ' ')

# printの途中は何も開けない
# printの最後に改行する（'\n'が改行を表わす特殊文字、これで１文字扱い）
print('の', MONTHS, 'ヶ月です。', sep = '', end = '\n')
print('---')

# カンマで区切ってリストを出力する例
shikoku_list = ['香川','愛媛','高知','徳島']
print('四国の都道府県は', end = '')
for ken in shikoku_list:
    # 最後のものにもカンマがついてしまうけど、今回はOKとします
    print(ken, end = ',')

# 間を開ける指定の代わりに、文字列にして１つに繋げてみる
print('の' + str(len(shikoku_list)) + 'つです。')

print( 1, 2, 3, sep = '-', end = ',' )
print( 4, 5, 6, sep = '')
