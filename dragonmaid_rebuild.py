#################################################################
#created by dynamder
#version:1.0.1
#date:2022.4.24
#Class 'DragWindow' is from https://github.com/arcticfox1919/tkinter-tabview/blob/master/dragwindow.py, with a little modification
#################################################################
from preset_windows.preset_windows import *

dragonmaid=Maid() #create a maid instance
print('maid create')
dragonmaid.hide() #the screen will not show the maid
dragonmaid.greet.show() # show a greeting picture
dragonmaid.show() #the maid appears

dragonmaid.root.mainloop()

input()


