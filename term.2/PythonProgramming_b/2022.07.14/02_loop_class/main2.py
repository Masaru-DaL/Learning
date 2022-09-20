# クラスと繰り返し
from match import Match

match_list = []

while True:
    # tryは、入力間違いをなかったことにするための準備
    # ※下記処理の説明は３学期になります
    try:

        print("=" * 70)
        print("「1:試合登録」「2:得点登録」「3:試合結果表示」"
              "「4:結果一覧表示」「9:終了」")
        menu = int(input("メニューを選んで下さい："))

        if menu == 1:
            op = input("相手チーム名：")
            match_list.append(Match(op))
            print(op + "との試合を登録しました。")
        elif menu == 2:
            if len(match_list) == 0:
                print("試合が登録されていません")
                continue

            for i, mt in enumerate(match_list):
                print(f"「{i+1}: vs{mt.op_team}戦」", end=" ")
            print()

            num = int(input("点数を登録する試合を選んで下さい："))
            mt = match_list[num - 1]
            my_s = int(input("自チームの得点を入力して下さい："))
            op_s = int(input("相手チームの得点を入力して下さい："))
            mt.record_score(my_s, op_s)
            print("得点を登録しました")


        elif menu == 3:
            if len(match_list) == 0:
                print("試合が登録されていません")
                continue

            for i, mt in enumerate(match_list):
                print(f"「{i+1}: vs{mt.op_team}戦」", end=" ")
            print()

            num = int(input("結果を表示したい試合を選んで下さい："))
            mt = match_list[num - 1]
            mt.result_output()

        elif menu == 4:
            print("＜試合結果一覧＞")
            for result in match_list:
                result.result_output()

        elif menu == 9:
            print("終了します")
            break

    # 入力間違いをなかったことにする
    # ※下記処理の説明は３学期になります
    except Exception as e:
        print(e)
        print("入力が間違えています。もう一度お願います。")
