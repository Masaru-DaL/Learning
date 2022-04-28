# 2022.04.28.PythonProgramming_a
# リストの作成
## 数字のリストを作成
num_list = [10, 15, 20, 30, 25, 45]
print(num_list)
print(len(num_list))

## 文字列のリストを作成
color_list = ['red', 'blue', 'yellow', 'green', 'pink']
print(color_list)
print(len(color_list))

## インデックスに対応した配列の取り出し
print(color_list[1])
print(color_list[-2])

## 配列の3~5を取り出す
print(eto_list[3:5])
## 配列の5~後ろ全部
print(eto_list[5:])

## 配列全部
print(eto_list[:])

## 後ろから逆に指定しまうとエラーになる
print(eto_list[-5:-3])

## 後ろから5番目から後ろへ
print(eto_list[-5:])

## 前から順に、後ろから5番目まで
print(eto_list[:-5])

## appendで最後に要素を追加
season_list = ['春', '夏', '秋', '冬']
season_list.append('次の春')
print(season_list)

## insertで指定したインデックスに要素を追加
season_list.insert(1, '梅雨')
print(season_list)

## 配列の中の指定したインデックスの要素を抜き出す
変数に抜き出した要素を格納できる(下記は変数pに格納)

eto_list = ['ね', 'うし', 'とら', 'う', 'たつ', 'み', 'うま', 'ひつじ', 'さる', 'とり', 'いぬ', 'い']

p = eto_list.pop(5)
print(p)
print(eto_list)

## 指定しないと一番最後の要素を抜き出す
p = eto_list.pop()
print(p)
print(eto_list)

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

# リストまとめ
- リスト
  - 変数 = [入れたい配列をカンマ区切りで入力]
- len
  - リストの配列数を表示
- インデックス番号に対応したリストの取り出し
  - 配列[0から始まるインデックス番号]
  - -(マイナス)で番号指定すると後ろから何番目、となる
- スライス
  - 指定した値の1個手前まで取得する
  - [1:5]
    - 1~4までを処理する
- 配列の最後に要素を追加
  - .append(追加する要素)
- 配列の中の指定したインデックスに要素を追加
  - .insert(インデックス番号, 追加する要素)
- .sort()
  - アルファベット順にソート
- .reverse()
  - 直前に並んでいた配列を逆順にソート
- del 変数
  - 削除
- in 変数
  - 真偽値で返す
- extend(リストなど)
  - 末尾にリストを追加する
- clear()
  - リストの要素をすべて削除する
- count(X)
  - リストにあるXという要素の数を取得する
- copy()
  - リストのコピーとなる、新しいリストを取得する

# Tips
- 文字列
  - 文字列も1文字1文字がリストのように扱われる
  - len(変数)
    - 文字列の長さ
  - 通常のリスト型とは異なり、何番目を何かに置き換えるなどの命令は出来ない
    - 変数自体を再代入する必要がある

# リストと処理の繰り返し
- listなどの複数の要素を持つデータとの組み合わせ

## for文でeto_listにある要素を変数etoに格納する
eto_list = ['ね', 'うし', 'とら', 'う', 'たつ', 'み', 'うま', 'ひつじ', 'さる', 'とり', 'いぬ', 'い']

for eto in eto_list:
  print(eto)

## rangeを使った場合
for i in range(len(eto_list)):
  print(eto_list[i])

## for文で取得した数を加算
month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
for all_day in month_day:
  total = total + all_day
print(total)

## sum関数を使って
day_sum = sum(month_day)
print(day_sum)

# Tips
- タプル
  - リストに類似した型
  - 何も付けずか、()で囲って定義する
  - 後から要素を変更することが出来ない
  - 複数の型が混在する場合などによく使われる
- 集合型(セット)
  - リストに類似した型
  - {}で囲む
  - set()
  - 重複する値を持たない
    - 重複した値が排除される
  - 順序が不定
    - セットした要素が順不同に並ぶ
  - 集合の考え方で、和、積、差、対称差といった演算が可能
- 辞書型
  - リストを拡張されたような型
  - キーと値がペア
  - 重複してはいけない
  - {}で囲み、キーと値の間には : を書く

## 辞書型, キーとバリューを格納
ordinals = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
print(ordinals)
print(ordinals['third'])

## バリューの指定は出来ない
print(ordinals[2])

## 要素の追加
ordinals['fifth'] = 5
print(ordinals)

## 既に要素があれば上書きする
ordinals['second'] = 20
print(ordinals)

## キーを指定して要素を削除
del ordinals['fourth']
print(ordinals)

# list()関数
- キーのリストが取得できる
ordinals = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

list1 = list(ordinals)
print(list1)
## 配列をソート
list2 = sorted(ordinals)
print(list2)

# items()関数
ordinals = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}

for eng, num in ordinals.items():
  print(eng)
  print(num)
