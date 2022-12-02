# class Character(pygame.sprite.Sprite):
#     # インスタンス化の際に配置場所を渡
#     def __init__(self, pos_x, pos_y):
#         pygame.sprite.Sprite.__init__(self)

#         # 画像ファイルのロード
#         _file_dir = os.path.dirname(__file__)
#         _sprite_sheet = pygame.image.load(os.path.join(_file_dir, "./images/$Fighter.png")).convert_alpha()

#         # 1枚の画像サイズを設定しておく
#         img_size_x, img_size_y = CHARA_SIZE_X, CHARA_SIZE_Y

#         '''subsurfaceを使用して画像の分割を行う
#         subsurfaceの引数は（開始x位置,開始y位置,横幅,立幅）
#         分割した画像を空のリストに追加'''
#         self._separate_images = []
#         for col in range(12):
#             img = _sprite_sheet.subsurface((img_size_x * col, 0, img_size_x, img_size_y))
#             self._separate_images.append(img)

#         # インデックスを設定。最初の画像と中心位置を設定
#         self.index = 0
#         self.image = self._separate_images[self.index]
#         self.rect = self.image.get_rect()
#         self.rect.center = (pos_x, pos_y)

#     # フレーム毎に行う処理をupdateに記載する
#     # indexをフレーム毎に1増やし、画像を切り替える
#     def update(self):
#         if self.index < len(self._separate_images):
#             self.image = self._separate_images[self.index]
#             self.index += 1
#         else:
#             self.index = 0
