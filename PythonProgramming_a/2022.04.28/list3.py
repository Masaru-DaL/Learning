season_list = ['春', '夏']
akihuyu_list = ['秋', '冬']

season_list = season_list + akihuyu_list
print(season_list)

season_list = season_list + ['一年']
print(season_list)

season_list[1] = 'なつ'
print(season_list)

season_list[2:4] = ['あき', 'ふゆ']
print(season_list)
