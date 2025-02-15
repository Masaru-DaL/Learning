# 飛行機ゲームの作成手順
## cave.pyの作成
1. ゲーム開始時の自機の位置
```python:
START_SHIP_X = 0
START_SHIP_Y = 250
```

2. 自機の上下方向の加速度
```python:
MY_SHIP_ACCELERATION = 2
```

3. 自機の位置
```python:
my_ship_pos = [START_SHIP_X, START_SHIP_Y]
```

4. 自機の上下方向の速度
```python:
my_ship_speed = 0
```

5. スペースキー押下フラグ
```python:
is_space_down = False
```

6. スペースキー押下で、フラグをTrueにする
```python:
elif event.type == KEYDOWN:
    if event.key == K_SPACE:
        is_space_down = True
```

7. 上下方向の自機の速度計算
```python:
if is_space_down:
    # 自機を上に加速
    my_ship_speed -= MY_SHIP_ACCELERATION
else:
    # 自機を下に加速
    my_ship_speed += MY_SHIP_ACCELERATION
```

8. 自機の位置を設定([1] -> y座標)
```python:
my_ship_pos[1] += my_ship_speed
```

9. 自機の描画
```python:
surface.blit(ship_image, my_ship_pos)
```

10. 壁の横幅
```python:
WALL_WIDTH = 10
```

11. 壁の穴のリストを作成する
```python:
holes = []
    # 壁(穴)の数は、画面横幅÷壁の横幅
    for x in range(W_WIDTH // WALL_WIDTH):
        # Rect -> 四角形
        holes.append(Rect(x * WALL_WIDTH, 20, WALL_WIDTH, 560))
```

12. 壁の描画
```python:
surface.fill((0, 255, 0))
```

13. 壁の穴の描画
```python:
for hole in holes:
    pygame.draw.rect(surface, (0, 0, 0), hole)
```

14. ゲームオーバーフラグ
```
python:is_gameover = False
```

15. ゲームプレイ中のみ以下の処理を行う
```python:
if not is_gameover:
```

7, 8を15内にインデントする。
```python:
# 15. ゲームプレイ中のみ以下の処理を行う
if not is_gameover:
    # 7. 上下方向の自機の速度計算
    if is_space_down:
        # 自機を上に加速
        my_ship_speed -= MY_SHIP_ACCELERATION
    else:
        # 自機を下に加速
        my_ship_speed += MY_SHIP_ACCELERATION

    # 8. 自機の位置を設定([1] -> y座標)
    my_ship_pos[1] += my_ship_speed
```

16. 壁にぶつかったか判定する(my_ship_pos[1] + 60は自機の高さ分を調整する)
```python:
# 「穴の上端より自機が上に行った場合」　または、
# 「穴の下端より自機の下端が下に行った場合」　にぶつかったとする
if holes[0].top > my_ship_pos[1] or holes[0].bottom < my_ship_pos[1] + 60:
    is_gameover = True
```

17. ゲームオーバーの場合は爆発画像を上から描画する(爆発画像の方が大きいので調整)
```python:
if is_gameover:
    surface.blit(clash_image, (my_ship_pos[0]-15, my_ship_pos[1]-30))
```

## hole.pyの作成
18. cave.pyと同じ階層に`hole.py`を作成する
`cave.py`からモジュールをコピペする
```python:
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE
```

19. Holeクラスを作成する
`cave.py`から壁の横幅を持ってくる。
```python:
class Hole:
    # 10. 壁の横幅
    WALL_WIDTH = 10
```

20. コンストラクタ
```python:
def __init__(self, x):
    self.rect = Rect(x, 20, Hole.WALL_WIDTH, 560)
```

## cave.pyの作成
21. Holeクラスのインポート
```python:
from hole import Hole
```

HoleクラスにWALL_WIDTHを定義したのでcave.pyの方は削除しておく。

22. Holeクラスのインスタンスを作成する
```python:
for x in range(W_WIDTH // Hole.WALL_WIDTH):
    holes.append(Hole(x * Hole.WALL_WIDTH))
```

23. Holeクラスの四角形を使用する
```python:
if holes[0].rect.top > my_ship_pos[1] or holes[0].rect.bottom < my_ship_pos[1] + 60:
```

24. クラスからrectを取得して描画
```python:
pygame.draw.rect(surface, (0, 0, 0), hole.rect)
```

## 当たり判定(壁)を移動させる処理
### hole.py
25. 穴のずれ角度
```python:
hole_angle = 1
```

26. 穴の設定
```python:
def set_hole(self, top, height):
    self.rect.top = top
    self.rect.height = height
```

27. 穴を角度分移動
```python:
def move_angle(self):
    # 穴を角度だけ移動する(move_ip(x, y))
    self.rect.move_ip(0, Hole.hole_angle)
```

28. 穴を左へ移動
```python:
def left_move(self):
    self.rect.move_ip(Hole.WALL_WIDTH * -1, 0)
```

### cave.py
29. 新しい穴を生成する
```python:
# 位置は一番右の穴の、1つ右にする
right_rect = holes[-1].rect
new_hole = Hole(right_rect.x + Hole.WALL_WIDTH)
# 新しい穴の位置とサイズを、一番右の穴と同じにする
new_hole.set_hole(right_rect.top, right_rect.height)
# 新しい穴を、角度分ずらす
new_hole.move_angle()
```

30. 先頭の穴を削除して、新しい穴を追加する
```python:
del holes[0]
    holes.append(new_hole)
```

31. 全ての穴を左に1つ分ずらす
```python:
for hole in holes:
    hole.left_move()
```

### hole.py
32. 画面の横幅
```python:
# (後でコメントアウト↓)
from cave import W_HEIGHT

W_HEIGHT = 0
```

### cave.py
33. Holeクラスのクラス変数に、ウィンドウの縦幅を設定
```python:
Hole.W_HEIGHT = W_HEIGHT
```

#### hole.py
34. randomのインポート
from random import randint

35. 壁の角度の最大値
```python:
ANGLE_MAX = 6
```

36. 穴をコピーして、一度動かしてみる
```python:
check_rect = self.rect.copy()
check_rect.move_ip(0, Hole.hole_angle)
# 移動後の位置が、上の端に達していたら新しい角度(下向き)を設定する
if check_rect.top <= 0:
    Hole.hole_angle = randint(1, Hole.ANGLE_MAX)
# 移動後の位置が、下の端に達していたら新しい角度(上向き)を設定する
elif check_rect.bottom >= Hole.W_HEIGHT:
    Hole.hole_angle = randint(1, Hole.ANGLE_MAX) * -1
```

37. 一段階ごとに穴が小さくなるサイズ
```python:
NARROW_SIZE = 10
```

38. 最小の穴のサイズ
```python:
MIN_HOLE_SIZE = 100
```

39. 穴のサイズの算出
```python:
def calc_hole_size(self):
    # 穴のサイズを計算
    self.hole_size = self.rect.height
    # 最小値を設定し、無限に小さくなるのを防ぐ
    if self.hole_size < Hole.MIN_HOLE_SIZE:
        self.hole_size = Hole.MIN_HOLE_SIZE
```

40. 穴のサイズを算出する
```python:
self.calc_hole_size()
# 40. 穴のサイズを計算後の値にする
self.rect.height = self.hole_size
```

41. 穴のサイズを算出する
```python:
self.calc_hole_size()
# 40. 穴のサイズを計算後の値にする
self.rect.top -= Hole.hole_angle
self.rect.height = self.hole_size
```

42. レベルを1増やす
```python:
# 42. レベル
level = 1

Hole.level += 1
```

if, elifの両方に実装

#### cave.py
43. スコア
```python:
score = 0
```

44. フォントを指定
```python:
game_font = pygame.font.SysFont("Arial", 32)
```

45. レベルとスコアの表示
```python:
level_info = game_font.render(f"Level: {Hole.level:3}", True,(0, 0, 255))
score_info = game_font.render(f"Score: {score:6}", True,(0, 0, 255))
surface.blit(level_info, (480, 20))
surface.blit(score_info, (620, 20))
```
{:3, :6}は桁数

46. ゲームオーバーでない場合、スコアを加算
```python:
else:
    score += 1
```
