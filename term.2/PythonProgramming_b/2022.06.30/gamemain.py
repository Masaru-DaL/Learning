from game_monster import GameMonster

slime = GameMonster()
slime.set_name("スライム")
slime.appear()

dragon = GameMonster()
dragon.set_name("ドラゴン")
dragon.appear()

print(type(slime)) # <class 'game_monster.GameMonster'>
