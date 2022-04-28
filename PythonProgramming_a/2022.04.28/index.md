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
