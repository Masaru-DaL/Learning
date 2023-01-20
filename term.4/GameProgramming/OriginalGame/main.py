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

def load_image(dir, filename, colorkey=None):
    file = os.path.join(dir, filename)
    image = pygame.image.load(file)
    image = image.convert()
    if not colorkey == None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image

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
        all_image = pygame.image.load(name).convert()

        ### 画像サイズ取得
        self.char_width  = all_image.get_width()
        self.char_height = all_image.get_height()

        ### キャラクターパターン格納
        for i in range(0, self.char_height, BLOCK_SIZE_HEIGHT):
            for j in range(0, self.char_width, BLOCK_SIZE_WIDTH):
                c_pattern = pygame.Surface((BLOCK_SIZE_WIDTH, BLOCK_SIZE_HEIGHT))
                c_pattern.blit(all_image, (0,0), (j,i,BLOCK_SIZE_WIDTH,BLOCK_SIZE_HEIGHT))
                c_pattern.set_colorkey((0,0,0))     # キャラクター画像の背景を透過させる
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

MAP1_COORDINATES_X = ()
MAP1_COORDINATES_Y = (330)

############################
### メイン関数
############################
def main():
    way = 0 # キーイベント変数
    map_flag = 1 # MAPフラグ：初期MAP1


    # 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)

    # 背景画像の取得
    map1_bg = pygame.image.load("./images/MAP1.png").convert()
    map2_bg = pygame.image.load("./images/MAP2.jpg").convert()

    # 画面サイズに合わせて画像を調整する
    fit_map1_bg = pygame.transform.scale(map1_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map2_bg = pygame.transform.scale(map2_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    map1_rect_bg = map1_bg.get_rect()
    map2_rect_bg = fit_map2_bg.get_rect()



    # キャラクター作成
    player = Character("./images/Player.png")
    # キャラクターの初期位置
    player_x = int(SCREEN_WIDTH/2)
    player_y = int(500)
    # playerSprite = pygame.sprite.Group(player)
    # playerSpriteRect = playerSprite.get_rect()

    # 時間オブジェクト生成
    clock = pygame.time.Clock()


    # 無限ループ
    while True:

        # フレームレート設定
        clock.tick(FRAME_RATE)

        # 背景設定
        if map_flag == 1:
            surface.blit(fit_map1_bg, map1_rect_bg)
        if map_flag == 2:
            surface.blit(fit_map2_bg, map2_rect_bg)

        # スプライト更新
        player.update(player_x, player_y, way)

        # スプライト描画
        player.draw(surface)

        # プレイヤーの座標
        player_coordinates = player.rect.center
        player_coordinates_x = player_coordinates[0]
        player_coordinates_y = player_coordinates[1]


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

                if map_flag == 1:
                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        if player_coordinates_y < SCREEN_HEIGHT-BLOCK_SIZE_HEIGHT/2:
                            player_y += CHARA_MOVE_SPEED
                            way = 0
                    if pressed_keys[K_LEFT]:
                        if player_coordinates_x > 0+BLOCK_SIZE_WIDTH/2:
                            player_x -= CHARA_MOVE_SPEED
                            way = 1
                    if pressed_keys[K_RIGHT]:
                        if player_coordinates_x < SCREEN_WIDTH-BLOCK_SIZE_WIDTH/2:
                            player_x += CHARA_MOVE_SPEED
                            way = 2
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        # MAP2に切り替わる場所に踏み入れた時
                        if player_coordinates_y < 330:
                            map_flag = 2
                            # MAP2の初期位置にplayerを配置する
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = int(SCREEN_HEIGHT-BLOCK_SIZE_HEIGHT/2)
                            way = 3
                            player.update(player_x, player_y, way)






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
