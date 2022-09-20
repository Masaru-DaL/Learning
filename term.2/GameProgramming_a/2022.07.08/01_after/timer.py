import tkinter

timer = 0

# カウントアップする関数
def count_up():
    global timer
    timer += 1
    t_label["text"] = timer
    root.after(10, count_up) # カウントアップ関数が呼ばれた後に1000ミリ秒ごとにカウントアップする

root = tkinter.Tk()
root.geometry("400x200")
t_label = tkinter.Label(font=("Ariel", 160))
t_label.pack()

# カウントアップ関数を呼ぶ
root.after(3000, count_up) # 3000ミリ秒後に1を表示する(約3秒)


root.mainloop()
