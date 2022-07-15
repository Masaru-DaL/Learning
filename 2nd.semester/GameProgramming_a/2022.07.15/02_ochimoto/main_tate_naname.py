# 並びチェック関数
def check_neko():
    for y in range(10):
        for x in range(8):
            check_field[y][x] = neko_field[y][x]
    
    # 横の並びをチェック（内側の６列のみ）
    for y in range(10):
        for x in range(1, 7):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合で
            # 左右ともに同じねこの場合
            if ch > 0 \
               and check_field[y][x-1] == ch \
               and check_field[y][x+1] == ch:
                # ３マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y][x-1] = 7
                neko_field[y][x+1] = 7

    # ２７）縦の並びをチェック（一番下と一番上以外）
    for y in range(1, 9):
        for x in range(8):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合で
            # 上下ともに同じねこの場合
            if ch > 0 \
               and check_field[y-1][x] == ch \
               and check_field[y+1][x] == ch:
                # ３マスとも肉球に変える
                neko_field[y][x] = 7
                neko_field[y-1][x] = 7
                neko_field[y+1][x] = 7
    # ２８）斜めの並びをチェック（一番外枠以外）
    for y in range(1, 9):
        for x in range(1, 7):
            # その場所のねこを取得
            ch = check_field[y][x]
            # マスにねこがいる場合
            if ch > 0:
                # 左上と右下がともに同じねこの場合
                if check_field[y-1][x-1] == ch \
                   and check_field[y+1][x+1] == ch:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x-1] = 7
                    neko_field[y+1][x+1] = 7
                # 右上と左下がともに同じねこの場合
                if check_field[y-1][x+1] == ch \
                   and check_field[y+1][x-1] == ch:
                    # ３マスとも肉球に変える
                    neko_field[y][x] = 7
                    neko_field[y-1][x+1] = 7
                    neko_field[y+1][x-1] = 7

