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
# リストまとめ
- リスト
  - 変数 = [入れたい配列をカンマ区切りで入力]
- len
  - リストの配列数を表示
- インデックス番号に対応したリストの取り出し
  - 配列[0から始まるインデックス番号]
  - -(マイナス)で番号指定すると後ろから何番目、となる
