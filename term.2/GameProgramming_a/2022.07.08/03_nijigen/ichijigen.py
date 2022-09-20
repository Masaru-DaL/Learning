import tkinter

list_a = [1,2,3,4,5,6,7,8,9,10,11,12]

root = tkinter.Tk()
root.geometry("400x300")
root.title("１次元リスト")

label = [None] * 12

# １次元リストを２次元に表示するためには、
# 横の数で「割って／余りを求めて」位置を調整する
for i in range(12):
    label[i] = tkinter.Label(
        root, text=list_a[i], width=2, height=1,
        font=("Ariel", 36), bg="lightyellow")
    px = (i % 4) * 100 + 10
    py = (i // 4) * 100 + 10
    label[i].place(x=px, y=py)

root.mainloop()
