# 演習3
# まず、student.pyにStudentクラスを作成して下さい。
#　Studentクラスの内容はstudent.pyに書いてあります。
#
# 続いて、このプログラムファイルに以下の処理を書きます。
# １）Studentクラスをインポートする
# ２）Studentクラスのインスタンスを２つ作る
#     それぞれ任意の「名前」と「最初の点数」を引数として渡す
# ３）好きな方のインスタンスに対してcheck_new_score関数を実行する
#     引数として新しい点数（任意の数）を渡す
# ４）もう一方のインスタンスに対してcheck_new_score関数を実行する
#     引数として新しい点数（任意の数）を渡す
#
# 上記まで出来たら、その後も３）や４）を繰り返して、
# 動作が想定通りか確認して下さい

from student import Student

student1 = Student("うかちゃん", 68)
student2 = Student("はるちゃん", 89)


student1.check_new_score(50)
student2.check_new_score(100)
