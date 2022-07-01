from unittest import result
from cat_check import CAT_CHECK_LIST     # ネコ度チェックリスト
from cat_check import CAT_CHECK_RESULT   # ネコ度チェック結果
import tkinter

CHECK_COUNT = 7

# ボタンが押された時の処理
def click_check():
  point = 0                              # チェックされた項目数
  for i in range(CHECK_COUNT):
    # チェックボックスのチェック分だけカウントを増やす
    if cat_check[i].get() == True:
      point += 1

  result_text.delete("1.0", tkinter.END)

  nekodo = int(100 * point / CHECK_COUNT)

  cat_result = "＜診断結果＞\nあなたのネコ度は"
  cat_result += f"{nekodo}%です。\n"
  cat_result += CAT_CHECK_RESULT[point]

  result_text.insert("1.0", cat_result)


root = tkinter.Tk()
root.title("(=^・・^=)")
root.resizable(False, False)            # ウィンドウズのサイズ変更の抑制(サイズ変更不可)

# キャンバスの作成
canvas = tkinter.Canvas(
  root,
  width=800, height=600
)
canvas.pack()

back_image = tkinter.PhotoImage(file = "image/cat_background.png")

canvas.create_image(
  0, 0,
  image = back_image,
  anchor = "nw"
)

# ボタンの部品を作成
check_button = tkinter.Button(
  root,
  text="診断する",
  font=("Arial", 32),
  bg="lightblue",
  command=click_check
)
check_button.place(x=400, y=480)      # ボタンの配置

# 結果表示用テキストエリアの作成
result_text = tkinter.Text(
  width=39, height=4,
  font=("Arial", 16),
)
result_text.place(x=320, y=30)        # テキストエリアを配置する

cat_check = [None] * CHECK_COUNT      # ネコ診断のチェック有無を入れるリスト
cat_cbtn = [None] * CHECK_COUNT       # ネコ診断のチェックボタンのリスト

for i in range(CHECK_COUNT):
  cat_check[i] = tkinter.BooleanVar() # ブール値オブジェクトを作成
  cat_check[i].set(False)             # チェックボックスをチェック無しにする

  # チェックボタンの部品を作成
  cat_cbtn[i] = tkinter.Checkbutton(
    root, text=CAT_CHECK_LIST[i],
    font=("Roman", 12),
    variable=cat_check[i],
    bg="#dfe"
  )
  cat_cbtn[i].place(x=400, y=160+40*i)


root.mainloop()
