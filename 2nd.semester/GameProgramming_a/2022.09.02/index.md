# 飛行機ゲームの作成手順
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

9.  自機の描画
```python:
surface.blit(ship_image, my_ship_pos)
```


