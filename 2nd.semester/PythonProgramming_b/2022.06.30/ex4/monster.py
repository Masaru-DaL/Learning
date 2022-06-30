# 演習４
# クラス「Monster」を作成します。
# このクラスには以下の関数を用意して下さい。
class Monster:

    # ・コンストラクタ(self, name, hp, power)
    #   引数に「name」「hp」「power」をもらい、
    #   それをそれぞれself.name、self.hp、self.powerに設定する
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    # ・damaged(self, damage)
    #   引数に「damage」をもらう
    #   self.hp から damage を引く
    #   self.hpが１以上の場合以下の文章を出力する
    #   「self.nameにdamage点のダメージを与えた！残りHP（self.hp）」
    #   self.hpが０以下の場合以下の文章を出力する
    #   「self.nameを倒した！」
    #   戻り値として、self.hpを返す
    def damaged(self, damage):

        self.hp = self.hp - damage

        if self.hp >= 1:
            print(f"{self.name}に{damage}点のダメージを与えた！残りHP({self.hp})")
        elif self.hp <= 0:
            print(f"{self.name}を倒した！")



    # ・attack(self)
    #   self.hp が0以下の場合は0を、
    #   そうでない場合はself.powerを戻り値として返す
    def attack(self):
        if self.hp <= 0:
            return 0
        else:
            return self.power
