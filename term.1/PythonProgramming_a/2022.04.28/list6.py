## 配列の中のインデックス番号を取得
moji_list = ['あ', 'い', 'う', 'え', 'お', 'あ', 'い', 'う', 'え', 'お']

idx = moji_list.index('お')
print(idx)

## 5番目から9番目にある'い'のインデックスを取得
idx = moji_list.index('い', 5, 9)
print(idx)

## 配列の中の一番最初の'い'を取得
moji_list.remove('い')
print(moji_list)
