#################################################################
#created by dynamder
#version:1.0.1
#date:2022.4.24
#basic windows for preset_windows
#DragWindow is from https://github.com/arcticfox1919/tkinter-tabview/blob/master/dragwindow.py, with a little modification
#################################################################

import tkinter as tk
from PIL import Image,ImageTk
class DragWindow: # define the window that can drag after overrideredirect()
    def __init__(self,size_show_width,size_show_height,title,is_tk=1):
        if is_tk==1:#is a tkinter main window?
            self.root = tk.Tk()
        elif is_tk==0:
            self.root=tk.Toplevel()
        #self.root.title(title)
        self.x, self.y = 0, 0
        self.title=title
        self.size_show_width=size_show_width
        self.size_show_height=size_show_height
        self.window_size = f'{size_show_width}x{size_show_height}'

        # 设置隐藏窗口标题栏和任务栏图标
        self.root.overrideredirect(True)
        # 窗口透明度60%
        self.root.attributes("-alpha", 0.4)
        # 设置窗口大小、位置 长x宽+x+y
        self.root.geometry(f"{self.window_size}+10+10")
        # 设定背景颜色
        self.root.configure(bg="blue")

        # 窗口移动事件
        self.root.bind("<B1-Motion>", self.move)
        # 单击事件
        self.root.bind("<Button-1>", self.get_point)

    def move(self, event):
        """窗口移动事件"""
        new_x = (event.x - self.x) + self.root.winfo_x()
        new_y = (event.y - self.y) + self.root.winfo_y()
        s = f"{self.window_size}+{new_x}+{new_y}"
        self.root.geometry(s)

    def get_point(self, event):
        """获取当前窗口位置并保存"""
        self.x, self.y = event.x, event.y



class Popwindow: # as the name implies
    def __init__(self,root,picture,width=200,height=150,sync_x=2,sync_y=2,interval=7):
        self.root=root
        self.dialog=tk.Toplevel()
        self.width=width
        self.height=height
        self.dialog.geometry(f"{self.width}x{self.height}")
        self.dialog.update()
        self.root.bind("<Configure>",self.sync_windows)# when the window is changed in position or size(here is position), sync the window
        self.diapic = Image.open(picture)
        self.diapic_sh = ImageTk.PhotoImage(self.diapic.resize((width, height), Image.ANTIALIAS))
        self.canvas = tk.Canvas(self.dialog, width=self.diapic.width, height=self.diapic.height, bg="gray")
        self.canvas.config(highlightthickness=0)
        self.sync_x=sync_x
        self.sync_y=sync_y
        print("sync_y:",sync_y)
        self.interval=interval

    def sync_windows(self,event):
        #x = self.root.winfo_x() + self.root.winfo_width() + self.sync_x
        #y = self.root.winfo_y()+self.sync_y
        x = self.root.winfo_x() -self.sync_x
        y = self.root.winfo_y()-self.sync_y
        self.dialog.geometry("+%d+%d" % (x, y))

    def show(self):
        self.dialog.attributes("-alpha", 1)  # 透明度(0.0~1.0)
        self.dialog.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
        self.dialog.attributes("-topmost", True)  # 永远处于顶层
        self.dialog.overrideredirect(True)  # 去除边框
        self.dialog.attributes("-transparentcolor", "gray")

        self.canvas.create_image(0, 0, image=self.diapic_sh, anchor="nw")
        self.canvas.pack()
        #self.start_Timer()
        #self.canvas.after(self.interval*1000,self.canvas.destroy())
        #self.dialog.after(self.interval*1000, self.dialog.destroy())

