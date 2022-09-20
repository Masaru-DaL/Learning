import tkinter

root = tkinter.Tk()
root.title("図形描画")
# キャンバスの作成、配置
canvas = tkinter.Canvas(root, width=500, height=500)
canvas.pack()

# 直線の書き方
canvas.create_line(100, 100, 300, 300, fill="blue", width=5)


# 直線の書き方２
canvas.create_line(100, 100, 200, 100, 100, 300, 400, 400,
                    fill="blue", width=5, smooth=True)

# 長方形の書き方
#canvas.create_rectangle(100, 100, 300, 300,
#                        fill="blue", outline="cyan", width=5)

# 円・楕円の書き方
#canvas.create_oval(200, 200, 450, 300,
#                   fill="pink", outline="red", width=5)

# 扇形の書き方
# canvas.create_arc(200, 200, 400, 400,
#                   fill="yellow", outline="orange", width=5,
#                   start=30, extent=300)

# 多角形の書き方
# canvas.create_polygon(100, 400, 400, 400, 300, 100,
#                    fill="pink", outline="red", width=5)

# 文字の書き方
# canvas.create_text(100, 250, text="文字",
#                    fill="darkred", font=("system", 24))






# ウィンドウの表示
root.mainloop()
