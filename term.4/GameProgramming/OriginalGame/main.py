# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
import random
import time

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
from pygame import mixer
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


class MySprite(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SURFACE.width:
            self.vx = -self.vx
        if self.rect.top < 330 or self.rect.bottom > SURFACE.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        self.rect = self.rect.clamp(SURFACE)
    #     pass
    #     # self.collision()
    #     character_rect = self.rect
    #     # player = Character("./images/Player.png")
    #     # player_rect = Character.player.get_rect()

    #     print("************************")
    #     print(character_rect)
    #     print(Character.get_rect())

    # def collision(self):

        # if character_rect == player_rect:
        #     print(player_rect)
        # self.rect.move_ip(self.vx, self.vy)
        # # 壁にぶつかったら跳ね返る
        # if self.rect.left < 0 or self.rect.right > SURFACE.width:
        #     self.vx = -self.vx
        # if self.rect.top < 0 or self.rect.bottom > SURFACE.height:
        #     self.vy = -self.vy
        # # 画面からはみ出ないようにする
        # self.rect = self.rect.clamp(SURFACE)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
    game_event = 0
    way = 0 # キーイベント変数
    map_flag = 0 # MAPフラグ：初期MAP1
    character_count = 0

    # 画面初期化
    pygame.init()
    surface = pygame.display.set_mode(SURFACE.size)

    pygame.mixer.init()
    pygame.mixer.music.load("./sound/game_event0.wav")
    pygame.mixer.music.play(-1)

    opening_font = pygame.font.SysFont("hg正楷書体pro", 70)
    press_key_font = pygame.font.SysFont("hg正楷書体pro", 30)
    font = pygame.font.SysFont("hg正楷書体pro", 20)

    # 背景色

    # 背景画像の取得
    map0_bg = pygame.image.load("./images/MAP0.jpg").convert()
    map1_bg = pygame.image.load("./images/MAP1.png").convert()
    map2_bg = pygame.image.load("./images/MAP2.jpg").convert()
    map3_bg = pygame.image.load("./images/MAP3.jpg").convert()
    map4_bg = pygame.image.load("./images/MAP4.jpg").convert()
    map5_bg = pygame.image.load("./images/MAP5.png").convert()
    map6_bg = pygame.image.load("./images/MAP6.png").convert()
    map10_bg = pygame.image.load("./images/MAP10.jpg").convert()
    map11_bg = pygame.image.load("./images/MAP11.png").convert()

    # 画面サイズに合わせて画像を調整する
    fit_map0_bg = pygame.transform.scale(map0_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map1_bg = pygame.transform.scale(map1_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map2_bg = pygame.transform.scale(map2_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map3_bg = pygame.transform.scale(map3_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map4_bg = pygame.transform.scale(map4_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map5_bg = pygame.transform.scale(map5_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map6_bg = pygame.transform.scale(map6_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map10_bg = pygame.transform.scale(map10_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
    fit_map11_bg = pygame.transform.scale(map11_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

    map0_rect_bg = map0_bg.get_rect()
    map1_rect_bg = map1_bg.get_rect()
    map2_rect_bg = fit_map2_bg.get_rect()
    map3_rect_bg = fit_map2_bg.get_rect()
    map4_rect_bg = fit_map2_bg.get_rect()
    map5_rect_bg = fit_map2_bg.get_rect()
    map6_rect_bg = fit_map2_bg.get_rect()
    map10_rect_bg = fit_map10_bg.get_rect()
    map11_rect_bg = fit_map10_bg.get_rect()

    # キャラクター作成
    player = Character("./images/Player.png")
    # キャラクターの初期位置
    player_x = int(SCREEN_WIDTH/2)
    player_y = int(500)

    # 1
    character1 = MySprite("./images/MAP1/C-Dullahan.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)

    # 2
    character2 = MySprite("./images/MAP2/CatPuppet-Green.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character3 = MySprite("./images/MAP2/Cockatrice-Blue.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character4 = MySprite("./images/MAP2/Fanatic-Green.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character5 = MySprite("./images/MAP2/Hornet-Red.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character6 = MySprite("./images/MAP2/Hound-Red.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)

    # 3
    character7 = MySprite("./images/MAP3/Gazer-Normal.png", int(random.uniform(50, 500)), int(random.uniform(400, 600)), 0, 0)
    character8 = MySprite("./images/MAP3/Ghost-Purple.png", int(random.uniform(50, 500)), int(random.uniform(400, 600)), 0, 0)

    # 4
    character9 = MySprite("./images/MAP4/C-YangMob.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character10 = MySprite("./images/MAP4/Goblin-Red.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character11 = MySprite("./images/MAP4/Wwolf_normal.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)

    # 5
    character12 = MySprite("./images/MAP5/Assassin-Blue.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character13 = MySprite("./images/MAP5/Bat-Black.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)
    character14 = MySprite("./images/MAP5/Hound-Normal.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)

    # 6
    character15 = MySprite("./images/MAP6/Mage-Red.png", int(random.uniform(50, 800)), int(random.uniform(400, 600)), 0, 0)

    # キャラクターをスプライトグループに追加する
    map2_character_group = pygame.sprite.RenderUpdates()
    map2_character_group.add(character2, character3, character4, character5, character6)

    map3_character_group = pygame.sprite.RenderUpdates()
    map3_character_group.add(character7, character8)

    map4_character_group = pygame.sprite.RenderUpdates()
    map4_character_group.add(character9, character10, character11)

    map5_character_group = pygame.sprite.RenderUpdates()
    map5_character_group.add(character12, character13, character14)

    map1_character_group = pygame.sprite.RenderUpdates()
    map1_character_group.add(character1)

    map6_character_group = pygame.sprite.RenderUpdates()
    map6_character_group.add(character15)

    # 時間オブジェクト生成
    clock = pygame.time.Clock()


    # 無限ループ
    while True:
        # フレームレート設定
        clock.tick(FRAME_RATE)

        # text
        opening_text = opening_font.render("Gathering Of Companions", True, (34, 139, 34))
        explanatory_text = press_key_font.render("各地に散らばる様々な種族の仲間を集めよう！", True, (255,255,255))
        game_clear_text = opening_font.render("CONGRATULATIONS!!", True, (0,0,205))
        game_over_text = opening_font.render("GAME OVER ...", True, (220,20,60))
        press_key_text = press_key_font.render("Press the space key.", True, (255,255,255))
        character_count_text = font.render("仲間の数；"+ str(character_count) + "/ 15", True, (0,0,0))


        # 背景設定
        if game_event == 0:
            surface.blit(fit_map0_bg, map0_rect_bg)
            surface.blit(opening_text, (100, 150))
            surface.blit(explanatory_text, (150, 650))
            surface.blit(press_key_text, (350, 550))
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        pygame.mixer.music.load("./sound/game_event1.wav")
                        pygame.mixer.music.play(-1)

                        game_event = 1
                        map_flag = 1
        elif game_event == 1:
            if character_count == 15:
                pygame.mixer.music.load("./sound/game_event2.wav")
                pygame.mixer.music.play(-1)
                game_event = 2
                map_flag = 10

            if map_flag == 6:
                if character_count < 14:
                    pygame.mixer.music.load("./sound/game_event3.wav")
                    pygame.mixer.music.play(-1)
                    player_x = -100
                    player_y = -100
                    game_event = 3
                    map_flag = 11
                else:
                    surface.blit(fit_map6_bg, map6_rect_bg)
                    surface.blit(character_count_text, (800, 10))

            if map_flag == 1:
                surface.blit(fit_map1_bg, map1_rect_bg)
                surface.blit(character_count_text, (800, 10))
            if map_flag == 2:
                surface.blit(fit_map2_bg, map2_rect_bg)
                surface.blit(character_count_text, (800, 10))
            if map_flag == 3:
                surface.blit(fit_map3_bg, map3_rect_bg)
                surface.blit(character_count_text, (800, 10))
            if map_flag == 4:
                surface.blit(fit_map4_bg, map4_rect_bg)
                surface.blit(character_count_text, (800, 10))
            if map_flag == 5:
                surface.blit(fit_map5_bg, map5_rect_bg)
                surface.blit(character_count_text, (800, 10))


        elif game_event == 3:
            surface.blit(fit_map11_bg, map11_rect_bg)
            surface.blit(game_over_text, (100, 150))

        elif game_event == 2:
            surface.blit(fit_map10_bg, map10_rect_bg)
            surface.blit(game_clear_text, (100, 150))


        # スプライト更新
        player.update(player_x, player_y, way)
        if game_event == 2:
            player.update(-100, -100, 0)

        # スプライト描画
        player.draw(surface)

        # プレイヤーの座標
        player_coordinates = player.rect.center
        player_coordinates_x = player_coordinates[0]
        player_coordinates_y = player_coordinates[1]

        # rect一覧
        player_rect = player.rect

        character1_rect = character1.rect
        character2_rect = character2.rect
        character3_rect = character3.rect
        character4_rect = character4.rect
        character5_rect = character5.rect
        character6_rect = character6.rect
        character7_rect = character7.rect
        character8_rect = character8.rect
        character9_rect = character9.rect
        character10_rect = character10.rect
        character11_rect = character11.rect
        character12_rect = character12.rect
        character13_rect = character13.rect
        character14_rect = character14.rect
        character15_rect = character15.rect

        if map_flag == 1:
            if character_count == 13:
                map1_character_group.update()
                map1_character_group.draw(surface)

                # キャラクター1の処理
                if map1_character_group.has(character1):
                    if player_rect.colliderect(character1_rect):
                        character1.remove(map1_character_group)
                        character_count += 1

        if map_flag == 2:
            map2_character_group.update()
            map2_character_group.draw(surface)

            # キャラクター2の処理
            if map2_character_group.has(character2):
                if player_rect.colliderect(character2_rect):
                    character2.remove(map2_character_group)
                    character_count += 1

            # キャラクター3の処理
            if map2_character_group.has(character3):
                if player_rect.colliderect(character3_rect):
                    character3.remove(map2_character_group)
                    character_count += 1

            # キャラクター4の処理
            if map2_character_group.has(character4):
                if player_rect.colliderect(character4_rect):
                    character4.remove(map2_character_group)
                    character_count += 1

            # キャラクター5の処理
            if map2_character_group.has(character5):
                if player_rect.colliderect(character5_rect):
                    character5.remove(map2_character_group)
                    character_count += 1

            # キャラクター6の処理
            if map2_character_group.has(character6):
                if player_rect.colliderect(character6_rect):
                    character6.remove(map2_character_group)
                    character_count += 1

        if map_flag == 3:
            map3_character_group.update()
            map3_character_group.draw(surface)

            # キャラクター7の処理
            if map3_character_group.has(character7):
                if player_rect.colliderect(character7_rect):
                    character7.remove(map3_character_group)
                    character_count += 1

            # キャラクター8の処理
            if map3_character_group.has(character8):
                if player_rect.colliderect(character8_rect):
                    character8.remove(map3_character_group)
                    character_count += 1

        if map_flag == 4:
            map4_character_group.update()
            map4_character_group.draw(surface)

            # キャラクター9の処理
            if map4_character_group.has(character9):
                if player_rect.colliderect(character9_rect):
                    character9.remove(map4_character_group)
                    character_count += 1
            # キャラクター10の処理
            if map4_character_group.has(character10):
                if player_rect.colliderect(character10_rect):
                    character10.remove(map4_character_group)
                    character_count += 1
            # キャラクター11の処理
            if map4_character_group.has(character11):
                if player_rect.colliderect(character11_rect):
                    character11.remove(map4_character_group)
                    character_count += 1

        if map_flag == 5:
            map5_character_group.update()
            map5_character_group.draw(surface)

            # キャラクター12の処理
            if map5_character_group.has(character12):
                if player_rect.colliderect(character12_rect):
                    character12.remove(map5_character_group)
                    character_count += 1
            # キャラクター13の処理
            if map5_character_group.has(character13):
                if player_rect.colliderect(character13_rect):
                    character13.remove(map5_character_group)
                    character_count += 1
            # キャラクター14の処理
            if map5_character_group.has(character14):
                if player_rect.colliderect(character14_rect):
                    character14.remove(map5_character_group)
                    character_count += 1

        if map_flag == 6:
            if character_count == 14:
                map6_character_group.update()
                map6_character_group.draw(surface)

                # キャラクター15の処理
                if map6_character_group.has(character15):
                    if player_rect.colliderect(character15_rect):
                        character15.remove(map6_character_group)
                        character_count += 1



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
                            player_y = int(SCREEN_HEIGHT-BLOCK_SIZE_HEIGHT)
                            way = 3
                            player.update(player_x, player_y, way)

                elif map_flag == 2:
                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        player_y += CHARA_MOVE_SPEED
                        way = 0
                        # MAP1に切り替わる場所に踏み入れた時
                        if player_coordinates_y > 700:
                            map_flag = 1
                            # MAP2の初期位置にplayerを配置する
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = 400
                            way = 0
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_LEFT]:
                        player_x -= CHARA_MOVE_SPEED
                        way = 1

                        if player_coordinates_x < 50:
                            map_flag = 5
                            player_x = SCREEN_WIDTH - 50
                            player_y = 600
                            way = 1
                            player.update(player_x, player_y, way)

                    if pressed_keys[K_RIGHT]:
                        player_x += CHARA_MOVE_SPEED
                        way = 2

                        if player_coordinates_x > SCREEN_WIDTH-50:
                            map_flag = 6
                            player_x = 50
                            player_y = 600
                            way = 2
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        # MAP2に切り替わる場所に踏み入れた時
                        if player_coordinates_y < 330:
                            map_flag = 3
                            # MAP2の初期位置にplayerを配置する
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = int(SCREEN_HEIGHT-BLOCK_SIZE_HEIGHT)
                            way = 3
                            player.update(player_x, player_y, way)

                elif map_flag == 3:
                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        player_y += CHARA_MOVE_SPEED
                        way = 0
                        # MAP1に切り替わる場所に踏み入れた時
                        if player_coordinates_y > 700:
                            map_flag = 2
                            # MAP2の初期位置にplayerを配置する
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = 400
                            way = 0
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_LEFT]:
                        player_x -= CHARA_MOVE_SPEED
                        way = 1
                        if player_coordinates_x < 30:
                            player_x += CHARA_MOVE_SPEED
                            way = 1
                    if pressed_keys[K_RIGHT]:
                        player_x += CHARA_MOVE_SPEED
                        way = 2
                        if player_coordinates_x > SCREEN_WIDTH-30:
                            player_x -= CHARA_MOVE_SPEED
                            way = 2
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        # MAP2に切り替わる場所に踏み入れた時
                        if player_coordinates_y < 370 and player_coordinates_x > 600:
                            player_y += CHARA_MOVE_SPEED
                        elif player_coordinates_y < 330:
                            map_flag = 4
                            # MAP2の初期位置にplayerを配置する
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = int(SCREEN_HEIGHT-BLOCK_SIZE_HEIGHT)
                            way = 3
                            player.update(player_x, player_y, way)

                elif map_flag == 4:
                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        player_y += CHARA_MOVE_SPEED
                        way = 0
                        if player_coordinates_y > SCREEN_HEIGHT-30:
                            map_flag = 3
                            player_x = int(SCREEN_WIDTH/2)
                            player_y = 400
                            way = 3
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_LEFT]:
                        player_x -= CHARA_MOVE_SPEED
                        way = 1
                        if player_coordinates_x < 30:
                            player_x += CHARA_MOVE_SPEED
                    if pressed_keys[K_RIGHT]:
                        player_x += CHARA_MOVE_SPEED
                        way = 2
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        if player_coordinates_y < 385:
                            player_y += CHARA_MOVE_SPEED

                elif map_flag == 5:
                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        player_y += CHARA_MOVE_SPEED
                        way = 0
                        # MAP1に切り替わる場所に踏み入れた時
                        if player_coordinates_y > SCREEN_HEIGHT-30:
                            player_y -= CHARA_MOVE_SPEED
                    if pressed_keys[K_LEFT]:
                        player_x -= CHARA_MOVE_SPEED
                        way = 1
                        if player_coordinates_x < 30:
                            player_x += CHARA_MOVE_SPEED
                    if pressed_keys[K_RIGHT]:
                        player_x += CHARA_MOVE_SPEED
                        way = 2
                        if player_coordinates_x > SCREEN_WIDTH-30:
                            map_flag = 2
                            player_x = 30
                            player_y = 400
                            way = 2
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        # MAP2に切り替わる場所に踏み入れた時
                        if player_coordinates_y < 385:
                            player_y += CHARA_MOVE_SPEED

                elif map_flag == 6:

                    # 方向キー
                    pygame.key.set_repeat(20, 30)
                    pressed_keys = pygame.key.get_pressed()
                    if pressed_keys[K_DOWN]:
                        player_y += CHARA_MOVE_SPEED
                        way = 0
                        # MAP1に切り替わる場所に踏み入れた時
                        if player_coordinates_y > 700:
                            if player_coordinates_y < SCREEN_HEIGHT-30:
                                player_y -= CHARA_MOVE_SPEED
                                way = 0
                    if pressed_keys[K_LEFT]:
                        player_x -= CHARA_MOVE_SPEED
                        way = 1
                        if player_coordinates_x < 30:
                            map_flag = 2
                            player_x = SCREEN_WIDTH-30
                            player_y = 400
                            way = 1
                            player.update(player_x, player_y, way)
                    if pressed_keys[K_RIGHT]:
                        player_x += CHARA_MOVE_SPEED
                        way = 2
                        if player_coordinates_x > SCREEN_WIDTH-30:
                            player_x -= CHARA_MOVE_SPEED
                            way = 2
                    if pressed_keys[K_UP]:
                        player_y -= CHARA_MOVE_SPEED
                        way = 3
                        # MAP2に切り替わる場所に踏み入れた時
                        if player_coordinates_y < 385:
                            player_y += CHARA_MOVE_SPEED


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
