import tkinter
from color import ColorPalette

root = tkinter.Tk()
root.title("カラーパレット")
# キャンバスの作成、配置
canvas = tkinter.Canvas(root, width=600, height=100)
canvas.pack()

color_list = ["red","orange","blue","pink","black","green","purple","gold","brown"]
pal = ColorPalette(color_list)

for i, col in enumerate(pal):
    # 長方形
    canvas.create_rectangle(50*i+10, 10, 50*i+50, 90, 
                            fill=col, width=0)


# ウィンドウの表示
root.mainloop()

