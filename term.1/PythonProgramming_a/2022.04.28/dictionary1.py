## 辞書型, キーとバリューを格納
from typing import OrderedDict


ordinals = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
print(ordinals)
print(ordinals['third'])

## バリューの指定は出来ない
# print(ordinals[2])

## 要素の追加
ordinals['fifth'] = 5
print(ordinals)

## 既に要素があれば上書きする
ordinals['second'] = 20
print(ordinals)

## キーを指定して要素を削除
del ordinals['fourth']
print(ordinals)
