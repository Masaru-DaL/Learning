# 空のリストを用意
stack_list = []

# 入力待ちの永久ループ
while True:
    print('---')
    print('現在のstack_list：', stack_list)
    cmd = input('何をしますか？[1:追加、2:取り出し、0:終了]')
    if cmd == '1':
        # 単語を入力してもらい、リストに追加する
        ch = input('追加する単語：')
        stack_list.append(ch)
    elif cmd == '2':
        # データが１つもない場合は、取り出しをしない
        if len(stack_list) == 0:
            print('データがありません')
            continue
        
        # 最後の単語を取り出す
        ch = stack_list.pop()
        print('単語「' + ch +'」を取り出しました')
    elif cmd == '0':
        # 終了する
        break
    else:
        # 他の場合は何もしない
        pass

