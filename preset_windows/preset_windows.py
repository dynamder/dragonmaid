#################################################################
#created by dynamder
#version:1.0.1
#date:2022.4.24
#windows for dragonmaid
#################################################################


import sys
import random

from base_windows.base_windows import *
from base_component.base_component import *
class Chatbubble(Popwindow): #maid will talk through this way, a subclass of Popwindow
    def __init__(self,root,picture,mate_sets,width=200,height=150,sync_x=2,sync_y=2,interval=7):
        # root:the chatbubble belongs to which,picture:the picture used for the chatbubble;width,height:the width and height of the chatbubble
        #sync_x,sync_y:offset for showing the picture; interval:the chatbubble will be withdrawn after interval seconds
        super(Chatbubble, self).__init__(root, picture, width, height, sync_x, sync_y, interval)
        self.words=list() # the word list the maid will say
        self.mate_sets=mate_sets
        with open(f'{self.mate_sets}/words.txt', encoding='utf-8') as words: #read words from local file
            for line in words:
                line1=line.rstrip('\n')
                line2=line1.replace(';','\n')
                self.words.append(line2)
        self.is_chatting=False
        self.sync_x=self.dialog.winfo_width()-sync_x
        self.sync_y=self.root.winfo_height()//3-self.dialog.winfo_height()+sync_y

    def sync_windows(self,event): #keep the relative position between the chatbubble and the maid
        # x = self.root.winfo_x() + self.root.winfo_width() + self.sync_x
        # y = self.root.winfo_y()+self.sync_y
        x = self.root.winfo_x() - self.sync_x
        y = self.root.winfo_y() +self.sync_y
        #self.dialog.geometry("+%d+%d" % (x, y))

        self.dialog.geometry("+%d+%d" % (x, y))


    def chat(self,event): #showing the bubbles and the words
        selec=random.randint(1, len(self.words)-1)
        self.text=self.words[selec]
        if self.is_chatting: #if a chatbubble exists, return
            return

        print("chat")
        #show the bubbles
        x = self.root.winfo_x() - self.sync_x
        y = self.root.winfo_y() + self.sync_y
        # self.dialog.geometry("+%d+%d" % (x, y))

        self.dialog.geometry("+%d+%d" % (x, y))
        self.dialog.update()
        self.show()
        #show the text
        self.text_show=self.canvas.create_text(30,30,text=self.text,font=("等线",11),anchor="nw")
        self.canvas.pack()
        self.dialog.deiconify()

        #sync the windows as the self.sync_window() is used as a callback function


        self.flip_state() #the state is turned to being shown
        self.dialog.after(7000,self.end)#withdraw the bubble and the words
        self.dialog.after(7050,self.flip_state) #turn the state to unshown


    def end(self):#withdraw the bubble and the words
        self.dialog.withdraw()
        self.canvas.delete(self.text_show)

    def flip_state(self): #flip between 'shown' and 'unshown'
        if self.is_chatting:
            self.is_chatting=False
        else:
            self.is_chatting=True

    def hide(self):
        self.dialog.withdraw()

class Min_maid(DragWindow): #the maid cannot interact with you in this mode
    def __init__(self,root,picture,width,height):
        #root:the father window;picture:the picture shown when entering this state
        #width,height:the picture will shown as (width,height)
        super().__init__(width,height,title='mini',is_tk=0)
        self.mini=self.root
        self.father=root

        self.mini.attributes("-alpha", 1)  # 透明度(0.0~1.0)
        self.mini.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
        self.mini.attributes("-topmost", True)  # 永远处于顶层
        self.mini.overrideredirect(True)  # 去除边框
        self.mini.attributes("-transparentcolor", "gray")

        self.picture=picture

        self.bt=Return_button(self.mini,self.father.root,picture=self.picture,text='call',width=250,height=150)# once the button activated, the interactive maid will reshow
        self.bt.activate()
        #self.bt=tk.Button(self.mini,width=300,height=150,text="呼唤",image=self.minipic_sh,command=self.calling)
        #self.bt.pack()
        self.mini.withdraw()

    def minimize(self):#enter the uninteractve mode
        self.mini.deiconify()

    def calling(self): # exit this mode
        self.father.root.deiconify()
        self.mini.withdraw()

class Maid(DragWindow): #the maid showed on your screen
    def __init__(self):
        self.read_config()#read necessary config information from a local file
        super().__init__(self.size_show_width,self.size_show_height,title='Maid',is_tk=1)
        self.scx = self.root.winfo_screenwidth()  # 获取当前屏幕的宽
        self.scy = self.root.winfo_screenheight()  # 获取当前屏幕的高
        self.greet = Maid_greet(self.scx, self.scy,self.greetpicture)

        self.root.attributes("-alpha", 1)  # 透明度(0.0~1.0)
        self.root.attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
        self.root.attributes("-topmost", True)  # 永远处于顶层
        self.root.overrideredirect(True)  # 去除边框
        self.root.geometry(f"{self.size_show_width}x{self.size_show_height}")
        #self.root.configure(bg="none")
        self.root.attributes("-transparentcolor", "gray")
        self.root.update()
        """self.bg_canvas=tk.Canvas(self.root,width=self.size_show_width,height=self.size_show_height,bd=0,highlightthickness=0)
        self.bg_image=Image.open('completely_transparent.png')
        self.bg_image_show=ImageTk.PhotoImage(self.bg_image.resize((self.size_show_width,self.size_show_height),Image.ANTIALIAS))
        self.bg_canvas.pack()"""

        self.picture = Image.open(self.picturename)
        self.picuture_show_png = ImageTk.PhotoImage(self.picture.resize((self.size_show_width,self.size_show_height),Image.ANTIALIAS))  # .resize((int(size_show_width), int(size_show_height)), resample=Image.ANTIALIAS)
        canvas1 = tk.Canvas(self.root, width=self.picture.width, height=self.picture.height, bg="gray")
        canvas1.config(highlightthickness=0)
        canvas1.create_image(0, 0, image=self.picuture_show_png, anchor="nw")
        # canvas1.create_image(dragonmaid.width, 0, image=dm_png, anchor="nw")
        canvas1.pack()
        self.sync_x=self.sync_x*self.size_show_width//self.sync_x_ref
        self.sync_y = self.sync_y * self.size_show_height // self.sync_y_ref
        self.chatting = Chatbubble(self.root, self.chatpicturename,self.mate_sets,sync_x=self.sync_x,sync_y=self.sync_y,width=self.bubble_width,height=self.bubble_height)#the chatting instance
        self.minshape=Min_maid(self,self.minname,self.min_width,self.min_height)#the uninteractive mode


        self.root.bind('<Button-1>',self.chatting.chat)

        self.mmenu=Rc_menu(picture=self.menuname,root=self.root,work_func=self.event_minimize,exec_func=self.exec_scripts,rest_func=self.quit,width=self.menu_width,height=self.menu_height,work_text=self.menu_command_work,exec_text=self.menu_command_exec,rest_text=self.menu_command_rest,cascade_text=self.menu_cascade)
        #the menu will show when right clicked


    def exec_scripts(self):#some extern scripts to extensify the maid's function
        pass

    def event_minimize(self):#enter the uninteractive mode
        self.minshape.mini.geometry(f'+{self.root.winfo_x()}+{self.root.winfo_y()}')
        self.minshape.minimize()
        self.hide()

    def hide(self):#hide the maid itself
        self.root.withdraw()
        self.chatting.hide()

    def event_hide(self,event):
        self.hide()

    def show(self):
        self.root.deiconify()

    def event_show(self,event):
        self.show()

    def quit(self):#quit this program
        self.root.quit()
        self.root.destroy()
        sys.exit()

    def apply_config(self,obj):#apply the config information read from the local file
        obj.strip()
        #print(obj)
        pos = obj.find('=')
        if pos == -1:
            return
        name, value = obj.split('=')
        if name == 'mate_show':
            self.picturename = value
        elif name == 'mate_min':
            self.minname = value
        elif name == 'mate_menu':
            self.menuname = value
        elif name == 'greet':
            self.greetpicture=value
        elif name=='mate_chat':
            self.chatpicturename=value
        elif name=='mate_show_width':
            print(value)
            self.size_show_width=int(value)
        elif name=='mate_show_height':
            self.size_show_height=int(value)
        elif name   =='mate_min_width':
            self.min_width=int(value)
        elif name=='mate_min_height':
            self.min_height=int(value)
        elif name=='mate_menu_width':
            self.menu_width=int(value)
        elif name=='mate_menu_height':
            self.menu_height=int(value)
        elif name=='mate_bubble_width':
            self.bubble_width=int(value)
        elif name=='mate_bubble_height':
            self.bubble_height=int(value)
        elif name=='sync_x':
            self.sync_x=int(value)
        elif name=='sync_y':
            self.sync_y=int(value)
        elif name=='sync_x_ref':
            self.sync_x_ref=int(value)
        elif name=='sync_y_ref':
            self.sync_y_ref=int(value)
        elif name=='menu_cascade':
            self.menu_cascade=value
        elif name=='menu_command_work':
            self.menu_command_work=value
        elif name=='menu_command_exec':
            self.menu_command_exec=value
        elif name=='menu_command_rest':
            self.menu_command_rest=value

    def read_config(self):
        with open(r'./config.ini', encoding='utf-8') as config:
            for line in config:
                line2=line.strip()
                # print(obj)
                pos = line2.find('=')
                if pos == -1:
                    return

                name, value = line2.split('=')
                if(name=="mate_sets"):
                    self.mate_sets=value

        with open(f'{self.mate_sets}/config.ini',encoding='utf-8') as config_set:
            for line in config_set:
                self.apply_config(line.rstrip('\n'))




class Maid_greet: # the greet picture shown when the program start
    def __init__(self,scx,scy,picture):
        self.root = tk.Toplevel()
        self.transparancy = 0.9
        self.root.wm_attributes("-alpha", self.transparancy)  # 透明度(0.0~1.0)
        self.root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
        self.root.wm_attributes("-topmost", True)  # 永远处于顶层

        self.width, self.height = scx//2, scy//2
        self.place_x = scx // 3
        self.place_y = scy // 4  # 位置以屏幕左上角为起始点(0,0)
        self.root.geometry(f'{self.width}x{self.height}+{self.place_x}+{self.place_y}')
        self.picture=picture
        # print(scx,scy)

        self.root.overrideredirect(True)  # 去除边框

    def show(self):
        self.img_open = Image.open(self.picture)
        self.img_png = ImageTk.PhotoImage(self.img_open.resize((self.width,self.height),Image.ANTIALIAS))
        self.label_img = tk.Label(self.root, image=self.img_png)
        self.label_img.pack()
        self.root.after(4000, self.root.withdraw)