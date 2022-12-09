# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

import os
import sys

# タイトル
pygame.display.set_caption("The Water Margin ")

CLOCK = pygame.time.Clock()
FRAME_RATE = 80
FRAME_POSE = 20 # ポーズフレーム

# 32*30
SCREEN_WIDTH = 960 # 32*30
SCREEN_HEIGHT = 720 # 48*15

CHARA_MOVE_SPEED = 5


BLOCK_SIZE_WIDTH = 32
BLOCK_SIZE_HEIGHT = 48

SURFACE = Rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

############################
### フィールドクラス
############################
class Field(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        self.image = pygame.image.load(name).convert()

        ### 画像サイズ変更
        self.image = pygame.transform.scale(self.image, (BLOCK_SIZE_WIDTH, BLOCK_SIZE_HEIGHT))

        ### キャラクターオブジェクト生成
        self.rect = self.image.get_rect()

        ### ブロック位置設定
        self.rect.left = x * (self.rect.width)
        self.rect.top  = y * (self.rect.height)

    # フィールドの描画
    def draw(self, surface):
        surface.blit(self.image, self.rect)


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
    def __init__(self, name):
        pygame.sprite.Sprite.__init__(self)

        ### ファイル読み込み
        all_image = pygame.image.load(name).convert_alpha()

        ### 画像サイズ取得
        self.char_width  = all_image.get_width()
        self.char_height = all_image.get_height()

        ### キャラクターパターン格納
        for i in range(0, self.char_height, BLOCK_SIZE_HEIGHT):
            for j in range(0, self.char_width, BLOCK_SIZE_WIDTH):
                c_pattern = pygame.Surface((BLOCK_SIZE_WIDTH, BLOCK_SIZE_HEIGHT))
                c_pattern.blit(all_image, (0,0), (j,i,BLOCK_SIZE_WIDTH,BLOCK_SIZE_HEIGHT))
                self.images.append(c_pattern)

        ### キャラクター初期設定
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    ############################
    ### キャラクター更新
    ############################
    def update(self, player_x, player_y, way):

        ### 画像切り替え
        self.image = self.images[int(self.frame / FRAME_POSE) + way * int(self.char_width / BLOCK_SIZE_WIDTH)]

        if self.flag == 0:
            self.frame += 1
        else:
            self.frame -= 1

        ### 繰り返し(images[0]→[1]→[2]→[1]→[0]→[1]...)
        if   self.frame >= len(self.images) / int(self.char_height / BLOCK_SIZE_HEIGHT) * FRAME_POSE:
            self.frame = FRAME_POSE * 2 - 1
            self.flag = 1
        elif self.frame < 0:
            self.frame = FRAME_POSE
            self.flag = 0

        # キャラクター位置
        self.rect.centerx = player_x
        self.rect.centery = player_y

    # キャラクター描画
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
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 7
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 8
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 9
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 10
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 11
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 12
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), # 13
        (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 9), # 14
    )

############################
### メイン関数
############################
def main():


    way = 0 # キーイベント変数

    # 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)


    # キャラクター作成
    player = Character("./images/$Fighter.png")
    # キャラクターの初期位置
    player_x = int(SCREEN_WIDTH/2)
    player_y = int(SCREEN_HEIGHT/2)
    # playerSprite = pygame.sprite.Group(player)
    # playerSpriteRect = playerSprite.get_rect()

    # 時間オブジェクト生成
    clock = pygame.time.Clock()

    # 無限ループ
    while True:

        # フレームレート設定
        clock.tick(FRAME_RATE)

        # 背景設定
        surface.fill((0,0,0))

        # スプライト更新
        player.update(player_x, player_y, way)

        # スプライト描画
        player.draw(surface)

        # 画面更新
        pygame.display.update()

        # イベント取得
        for event in pygame.event.get():
            # 終了処理
            if event.type == QUIT:
                exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()

                # 方向キー
                pygame.key.set_repeat(20, 30)
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_DOWN]:
                    player_y += CHARA_MOVE_SPEED
                    way = 0
                if pressed_keys[K_LEFT]:
                    player_x -= CHARA_MOVE_SPEED
                    way = 1
                if pressed_keys[K_RIGHT]:
                    player_x += CHARA_MOVE_SPEED
                    way = 2
                if pressed_keys[K_UP]:
                    player_y -= CHARA_MOVE_SPEED
                    way = 3


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


############################
### キーイベントチェック処理関数
############################
def check_event():
    keymap = []
    # イベント処理ループ
    for event in pygame.event.get():
        # 終了処理
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # # キーダウン処理
        # elif event.type == KEYDOWN:
        #     if not event.key in keymap:
        #         keymap.append(event.key)
        # # キーアップ処理
        # elif event.type == KEYUP:
        #     keymap.remove(event.key)

############################
### 終了関数
############################
def exit():
    pygame.quit()
    sys.exit()

############################
### メイン関数呼び出し
############################
if __name__ == "__main__":
    main()
