# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import sys

# タイトル
pygame.display.set_caption("The Water Margin ")

# 32*30
SCREEN_WIDTH = 960 # 32*30
SCREEN_HEIGHT = 720 # 48*15

def main():
    pygame.init()                                   # Pygameの初期化
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # 背景画像の取得
    bg = pygame.image.load("./images/background_image.png").convert_alpha()
    rect_bg = bg.get_rect()

     # プレイヤー画像の取得
    player = pygame.image.load("./images/fighter1.png").convert_alpha()
    rect_player = player.get_rect()
    rect_player.center = (300, 480) # プレイヤー画像の初期位置


    while True:
        pygame.display.update()
        pygame.time.wait(30)
        screen.fill((0,0,0))        # 画面を黒色(#000000)に塗りつぶし
        screen.blit(bg, rect_bg)            # 背景画像の描画
        screen.blit(player, rect_player)    # プレイヤー画像の描画

        # イベント処理
        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()


if __name__ == "__main__":
    main()
