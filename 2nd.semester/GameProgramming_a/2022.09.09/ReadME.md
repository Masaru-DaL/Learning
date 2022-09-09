# ヘビゲームの変更点
1. 蛇の色の変更
`snake.py`
Snakeクラスに追加
ヘビの色をリストで何種類か用意し、その中からヘビの色をランダムで決定する。

2. ゲーム速度の変更
`main.py`
clock.tick(5)

3. エサを写真に変更
```python:
def draw(self, surface, width, height):
        # エサの数だけ、丸を描画する
        for pos in self.food_list:
            surface.blit(Foods.food_image, (pos[0]*width, pos[1]*height))
```

4. 画面の色の変更
`surface.fill((152,251,152))`
