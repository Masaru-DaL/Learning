# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

import os
import sys

# タイトル
pygame.display.set_caption("The Water Margin ")

CLOCK = pygame.time.Clock()
FRAME_RATE = 60
FRAME_POSE = 20 # ポーズフレーム

# 32*30
SCREEN_WIDTH = 960 # 32*30
SCREEN_HEIGHT = 720 # 48*15

CHARA_SIZE_WIDTH = 32
CHARA_SIZE_HEIGHT = 48

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

############################
### キャラクタークラス
############################
class Character(pygame.sprite.Sprite):

    ### クラス変数
    frame  = 0      # フレーム
    flag   = 0      # 切り替えフラグ
    images = []     # 画像リスト

    ############################
    ### 初期化メソッド
    ############################
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        all_image = pygame.image.load(name).convert_alpha()

        ### 画像サイズ取得
        self.char_width  = all_image.get_width()
        self.char_height = all_image.get_height()

        ### キャラクターパターン格納
        for i in range(0, self.char_height, CHARA_SIZE_HEIGHT):
            for j in range(0, self.char_width, CHARA_SIZE_WIDTH):
                c_pattern = pygame.Surface((CHARA_SIZE_WIDTH, CHARA_SIZE_HEIGHT))
                c_pattern.blit(all_image, (0,0), (j,i,CHARA_SIZE_WIDTH,CHARA_SIZE_HEIGHT))
                self.images.append(c_pattern)

        ### キャラクター初期設定
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=(x,y))

    ############################
    ### キャラクター更新
    ############################
    def update(self, way):

        ### 画像切り替え
        self.image = self.images[int(self.frame / FRAME_POSE) + way * int(self.char_width / CHARA_SIZE_WIDTH)]

        if self.flag == 0:
            self.frame += 1
        else:
            self.frame -= 1

        ### 繰り返し(images[0]→[1]→[2]→[1]→[0]→[1]...)
        if   self.frame >= len(self.images) / int(self.char_height / CHARA_SIZE_HEIGHT) * FRAME_POSE:
            self.frame = FRAME_POSE * 2 - 1
            self.flag = 1
        elif self.frame < 0:
            self.frame = FRAME_POSE
            self.flag = 0

    ############################
    ### キャラクター描画
    ############################
    def draw(self, surface):
        surface.blit(self.image, self.rect)

### マップ

MAP1 = (
#######  0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29  #####
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 0
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 1
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 2
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 3
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 4
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 5
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 6
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 7
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 8
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 9
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 10
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 11
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 12
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 13
        (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), # 14
    )

class Main:
    def __init__(self):
        pygame.init()

        player = Character("./images/$Fighter.png", int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT/2))
        self.characterSprite = pygame.sprite.Group(player)
        # # インスタンス化 + 配置場所
        # player = Character(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # # spritegroupに格納する。groupに入れると何かと便利
        # self.characterSprite = pygame.sprite.GroupSingle(player)

    def main(self):
        way = 0 # キーイベント変数

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    ### 方向キー
                    if event.key == K_DOWN:   # 下
                            way = 0
                            move_ip(0, 1)
                    if event.key == K_LEFT:   # 左
                            way = 1
                    if event.key == K_RIGHT:  # 右
                            way = 2
                    if event.key == K_UP:     # 上
                            way = 3

            SCREEN.fill((0,0,0))

            # ここで次の画像が用意される
            self.characterSprite.update(way)

            #グループを画面に描画
            self.characterSprite.draw(SCREEN)


            pygame.display.update()
            CLOCK.tick(FRAME_RATE)
        pygame.quit()
        sys.exit()

main = Main()


    # # 背景画像の取得
    # bg = pygame.image.load("./images/background_image.png").convert_alpha()
    # rect_bg = bg.get_rect()

    # # プレイヤー画像の取得
    # player = pygame.image.load("./images/fighter1.png").convert_alpha()
    # rect_player = player.get_rect()
    # rect_player.center = (300, 480) # プレイヤー画像の初期位置


    # while True:
    #     pygame.display.update()
    #     pygame.time.wait(30)

    #     screen.blit(bg, rect_bg)            # 背景画像の描画
    #     screen.blit(player, rect_player)    # プレイヤー画像の描画


if __name__ == "__main__":
    main.main()
