# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *

import os

# タイトル
pygame.display.set_caption("The Water Margin ")

CLOCK = pygame.time.Clock()
FPS = 5

# 32*30
SCREEN_WIDTH = 960 # 32*30
SCREEN_HEIGHT = 720 # 48*15

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Character(pygame.sprite.Sprite):
    # インスタンス化の際に配置場所を渡
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        # 画像ファイルのロード
        _file_dir = os.path.dirname(__file__)
        _sprite_sheet = pygame.image.load(os.path.join(_file_dir, "./images/Fighter.png")).convert_alpha()

        # 1枚の画像サイズを設定しておく
        img_size_x, img_size_y = 32, 48

        '''subsurfaceを使用して画像の分割を行う
        subsurfaceの引数は（開始x位置,開始y位置,横幅,立幅）
        分割した画像を空のリストに追加'''
        self._separate_images = []
        for col in range(3):
            img = _sprite_sheet.subsurface((img_size_x * col, 0, img_size_x, img_size_y))
            self._separate_images.append(img)

        # インデックスを設定。最初の画像と中心位置を設定
        self.index = 0
        self.image = self._separate_images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    # フレーム毎に行う処理をupdateに記載する
    # indexをフレーム毎に1増やし、画像を切り替える
    def update(self):
        if self.index < len(self._separate_images):
            self.image = self._separate_images[self.index]
            self.index += 1
        else:
            self.index = 0

class Main:
    def __init__(self):
        pygame.init()

        # インスタンス化 + 配置場所
        player = Character(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # spritegroupに格納する。groupに入れると何かと便利
        self.characterSprite = pygame.sprite.GroupSingle(player)

    def main(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

            SCREEN.fill((0,0,0))

            #グループを画面に描画
            self.characterSprite.draw(SCREEN)
            # ここで次の画像が用意される
            self.characterSprite.update()

            pygame.display.update()
            CLOCK.tick(FPS)
        pygame.quit()

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
