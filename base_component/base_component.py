#################################################################
#created by dynamder
#version:1.0.1
#date:2022.4.24
#base component used in preset_windows
#################################################################


import tkinter as tk
from PIL import Image,ImageTk
import os
import subprocess
class Super_button: #a more beatiful button created by using tk.canvas
    def __init__(self,root,picture,text,width,height):
        self.image = Image.open(picture)
        self.image_sh= ImageTk.PhotoImage(self.image.resize((width, height), Image.ANTIALIAS))
        self.text=text
        self.root=root
        #self.win=tk.Toplevel()
        self.canvas=tk.Canvas(self.root,width=width,height=height,bg="gray")
        self.root.attributes("-transparentcolor", "gray")
        self.canvas.config(highlightthickness=0)

        self.canvas.create_image(0, 0, image=self.image_sh, anchor="nw")

        self.canvas.bind('<Button-3>',self.handler)

    def handler(self,event):#when the 'button' is activated, execute this function
        pass

    def activate(self):
        self.canvas.pack()

    def deactivate(self):
        self.root.withdraw()

class Return_button(Super_button):# a Super_button used to exit the maid's uninteractive mode
    def __init__(self,root,reshownee,picture,text,width,height):
        #reshownee:the object that will be reshown
        super().__init__(root,picture,text,width,height)
        self.reshownee=reshownee

    def handler(self,event):
        self.reshownee.deiconify()
        self.deactivate()

class Rc_menu:#right_click menu
    def __init__(self,picture,root,work_func,exec_func,rest_func,width,height,cascade_text,work_text,exec_text,rest_text):
        self.root=root
        self.menubar = tk.Menu(self.root,tearoff=False)  # #创建菜单条
        self.xMenu = tk.Menu(self.menubar, tearoff=False)  # #创建子菜单
        self.width=width
        self.height=height
        self.picture_inner=Image.open(picture)
        self.picture=ImageTk.PhotoImage(self.picture_inner.resize((self.width,self.height),Image.ANTIALIAS))
        self.xMenu.add('cascade',image=self.picture)

        self.work_func=work_func
        self.exec_func=exec_func
        self.rest_func=rest_func

        self.xMenu.add_separator()
        self.xMenu.add_command(label=work_text,command=self.work_func)

        self.xMenu.add_separator()

        self.scripts = tk.Menu(self.xMenu, tearoff=False)
        self.exec_scripts = []
        i = -1
        for curdir, dirs, file in os.walk(r"./Scripts"):
            for dir in dirs:
                i += 1
                self.exec_scripts.append(str(dir))
                for files in os.listdir(f'./Scripts/{dir}'):
                    if files.endswith(".exe"):
                        print("i:",i)
                        self.scripts.add_command(label=str(dir), command=lambda i=i: self.script_exe(i))
                    elif files.endswith(".py"):
                        print("i:", i)
                        self.scripts.add_command(label=str(dir), command=lambda i=i: self.script_py(i))


        self.xMenu.add_cascade(label=exec_text, menu=self.scripts)

        self.xMenu.add_separator()
        self.xMenu.add_command(label=rest_text,command=self.rest_func)


        self.menubar.add_cascade(label=cascade_text, menu=self.xMenu)  # #创建总菜单，将子菜单绑定进来
        self.root.bind("<Button-3>", self.xShowMenu)  # #设定鼠标右键触发事件，调用xShowMenu方法

        #self.scripts=tk.Menu(self.scripts,tearoff=False)


    def script_exe(self,id):
        mcwd=os.getcwd()
        #print(f'{mcwd}\Scripts\{self.exec_scripts[id]}\exec.exe')
        os.system("chcp 65001")
        subprocess.Popen(f'.\Scripts\{self.exec_scripts[id]}\exec.exe',shell=False,cwd=mcwd)
        #print(r_v)

    def script_py(self,id):
        mcwd=os.getcwd()
        os.system("chcp 65001")
        subprocess.Popen(f'python ./Scripts/{self.exec_scripts[id]}/exec.py',shell=False,cwd=mcwd)

    def xShowMenu(self,event):
        self.menubar.post(event.x_root, event.y_root)  # #将菜单条绑定上事件，坐标为x和y的root位置


