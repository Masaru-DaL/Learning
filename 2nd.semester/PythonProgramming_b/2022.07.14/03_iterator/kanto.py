class Kanto:
    
    TOKEN_LIST = ["神奈川","東京","千葉","埼玉","群馬","栃木","茨城"]
    
    def __init__(self):
        self.i = 0
        
    def __next__(self):
        # 要素数をオーバーする場合、下記のエラーを発生させる
        # ※イテレーターには必須の処理
        if self.i >= len(Kanto.TOKEN_LIST):
            raise StopIteration()
        
        token = Kanto.TOKEN_LIST[self.i]
        self.i += 1
        return token
