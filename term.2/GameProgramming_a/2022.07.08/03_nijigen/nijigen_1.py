import tkinter

# リストの中にリストが入っている、２次元リスト
list_xy = [
    ["a1", "a2", "a3", "a4"],
    ["b1", "b2", "b3", "b4"],
    ["c1", "c2", "c3", "c4"],
]

root = tkinter.Tk()
root.geometry("400x300")
root.title("２次元リスト")

label = [None] * 12
i=0

# ２次元リストを表示するためには、
# 「横方向」と「縦方向」で、２重にループする

# 外側のリストで繰り返し
for y in range(3):
    # リストの中から、順にリストを取得する
    list_x = list_xy[y]
    print(list_x)
    
    # 内側のリストで繰り返し
    for x in range(4):
        label[i] = tkinter.Label(
            root, text=list_x[x], width=2, height=1,
            font=("Ariel", 36), bg="lightyellow")
        px = x * 100 + 10
        py = y * 100 + 10
        label[i].place(x=px, y=py)
        i += 1

root.mainloop()
