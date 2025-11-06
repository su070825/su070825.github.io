import tkinter as tk
import random
import threading
import time
import sys
bg_colors=["lightblue","lightgreen","lightyellow","pink","purple"]
tips=["要天天开心！！","不可以不吃饭！","我很想很想你","我想见面","要放假啦","要早点睡觉！！","一切都会变好哒","明年一定见","我比你想象的还要在乎你","要好好照顾自己呢！","平安顺遂","要相信自己嗷","我在天津很想你","想我了嘛","顺顺利利！！","烦恼消失！！"]
windows=[]
def show_warm_tip():
    window=tk.Tk()
    windows.append(window)
    screen_width=window.winfo_screenwidth()
    screen_height=window.winfo_screenheight()
    window_width=280
    window_height=60
    x=random.randrange(0,screen_width-window_width)
    y=random.randrange(0,screen_height-window_height)
    window.title("温馨提示")
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    tip=random.choice(tips)
    bg_color=random.choice(bg_colors)
    tk.Label(window,text=tip,bg=bg_color,font=("微软雅黑",16),width=30,height=3).pack()
    window.attributes('-topmost',True)
    window.bind('<space>',lambda event:close_all_windows())
    window.mainloop()
def close_all_windows():
    for window in windows:
        window.destroy()
    sys.exit()
    threads=[]
    for i in range(5):
        t=threading.Thread(target=show_warm_tip)
        threads.append(t)
        time.sleep(0.5)
        t.start()
