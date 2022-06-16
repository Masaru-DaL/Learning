# 演習０のｃ

# ex0_c_mod.py に別モジュールが用意してあります。

# 文字列を１つ入力してもらいます
# ex0_c_mod.pyに用意された関数「str_rev()」に
# 入力された文字を渡して下さい。
# すると、逆向きになったものが戻り値として返されます。
#
# 「（入力された文字） を逆にすると（戻り地の文字） です」と出力して下さい。

# 続きのプログラムを書いて下さい
import ex0_c_mod

from ex0_c_mod import str_rev

str_input = input("文字列を入力してください：")

str_r = str_rev(str_input)

print(str_input + "を逆にすると" + str_r + "です")
