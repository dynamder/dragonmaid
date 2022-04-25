# Dragonmaid_rebuild  v1.0.0

这是一个桌面宠物程序，纯python开发

亮点是几乎所有能显示出来的东西都可以自定义

现在似乎只能当个吉祥物，但扩展性脚本功能开发完成后说不定也可以上天入地无所不能呢（笑）

**不定期更新，但不会弃坑的**

作者：dynamder

版本号:1.0.1

更新日期:2022.4.24

可以从[这里](https://gitee.com/dynamder/dragonmaid/tree/master)获取

#### 更新内容

修复了一些bug，改进了配置文件，可以更加方便的切换角色形象了

------

**使用说明**

p.s.如果遇到技术问题或使用有困难的私聊我就好

这是项目的目录结构

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220424230348297.png" alt="image-20220424230348297" style="zoom:33%;" />



configs文件夹里存的是各种“角色包”，结构类似于这样

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220424230534985.png" alt="image-20220424230534985" style="zoom:25%;" /><img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220424230557940.png" alt="image-20220424230557940" style="zoom:25%;" />

Scripts文件夹里存放功能性脚本（还在路上就是了）



根目录下的config.ini用于选定“角色包”，如下图（没错内容就这么短短一行）

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220424230744370.png" alt="image-20220424230744370" style="zoom:25%;" />

可执行文件在项目根目录中*dist/dragonmaid_rebuild*（这个目录以下称为运行目录）处找到，双击运行该目录下的dragonmaid_rebuild.exe即可(如果是32位的电脑在*32-bit-dist*下）



点击后会出来一个可爱的家伙

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423233550087.png" alt="image-20220423233550087" style="zoom: 25%;" />

------

右键后会出现带有“吩咐”字样的菜单，单击后会出现带有“去工作”，“去执行”，“去休息”字样的条目

**去工作**：最小化（好吧其实也没小多少，日后可能会添加隐藏到托盘的功能），最小化状态下不会进行对话，在最小化状态下右键可以退出最小化状态

**去执行**：执行一些功能性脚本（开发中）

**去休息**：退出程序

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423233641365.png" alt="image-20220423233641365" style="zoom:25%;" />

------

左键单击可以让其说话，拖拽可以移动其在屏幕上的位置

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423233749364.png" alt="image-20220423233749364" style="zoom:25%;" />

------

运行目录下中configs文件夹存储角色包，里面pictures文件夹存储使用到的图片，Scripts文件夹下存储扩展性功能脚本（该功能仍在开发），以及对话词（words.txt）

如果大家像我一样对美工不太在行的找完想要的图片后可以用[这个网站](https://picwish.cn/?chn-piccpa)自动抠图（背景最好别太花否则得手动进行）



运行目录下的config.ini是配置文件，图片更换，显示大小控制可以修改其中参数来实现，已经提供了一份能正确运行的参数示例（如下）

------

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220424230240311.png" alt="image-20220424230240311" style="zoom:40%;" />





------

**config.ini（这里指的是角色包内的config.ini）内参数详解：**

mate_show:上文所述的可爱的家伙使用的图片(这家伙↓↓↓)

<img src="C:\Users\atomt\Desktop\image-20220423234139776.png" alt="image-20220423234139776" style="zoom:33%;" />

------

mate_min:可爱的家伙最小化后显示的图片

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423234406387.png" alt="image-20220423234406387" style="zoom: 25%;" />   →<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423234452434.png" alt="image-20220423234452434" style="zoom:33%;" />

------

mate_menu:右键菜单中显示的图片（如上图）

------

mate_chat:左键单击后对话框的图片

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423234751166.png" alt="image-20220423234751166" style="zoom: 33%;" />

------

greet：双击exe后屏幕中央出现的大图

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423234930745.png" alt="image-20220423234930745" style="zoom: 25%;" />

------

mate_show_width:小可爱显示时的长（水平方向，红色）

mate_show_height：小可爱显示时的宽（竖直方向，蓝色）

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423235259134.png" alt="image-20220423235259134" style="zoom:33%;" />

箭头表示正方向，单位：像素

------

mate_min_width:最小化时的显示长（水平方向，红色）

mate_min_height:最小化时的显示宽（竖直方向，蓝色）

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423235458121.png" alt="image-20220423235458121" style="zoom:33%;" />

箭头为正方向，单位：像素

------

mate_menu_width:菜单栏显示图片的长（水平方向，红色）

mate_menu_height:菜单栏显示图片的宽（竖直方向，蓝色）

<img src="C:\Users\atomt\AppData\Roaming\Typora\typora-user-images\image-20220423235717212.png" alt="image-20220423235717212" style="zoom:33%;" />

箭头为正方向，单位：像素

------

*注：图片显示时会根据设定的尺寸自动缩放*



words.txt编写详解

1.每一句话一行

2.一句话中每十个字符后加上";"(英文半角)

示例（以下为合法的words.txt内容）：

这是测试

这是一个超过10个字;符的测试

这是测试，这是测试，;这是测试，这是测试，;这是测试，这是测试，;这是测试，



------

**目前仍存在的问题**

1.透明背景色为灰色(0x808080)，因此如果图片中有灰色(0x808080)的话可能会有点小问题，可以替换成极为相似的颜色

------



**说些题外话**

想到要做一个这样的项目其实还挺早的，那时还不知道有tkinter这个方便的库（虽然说方便是有代价的。。），然后就咕掉了

然后某一天我成为了牌佬用上了某一套卡组（不太想暴露使用的卡组但是懂得应该都懂），然后就想做一些有关这些小可爱们的东西，然后就想起了曾经被我在筹划阶段就咕掉的项目，又阴差阳错的发现了tkinter这个库并且它竟然已经是python自带的库了。。

于是就开始了这么一个粗糙的小型项目



为什么叫dragonmaid呢，额，本来没想着扩展出去自定义功能的，但因为我个人比较喜欢写轮子的缘故发现复用性好像还不错（雾)，懒得改名了就这样吧



为什么还有rebuild呢，这是因为在内部测试的时候发现代码太乱了然后就重构了，虽然说对大家来说看的一定很奇怪（笑）



感觉效果上不是特别惊艳？可能的一个原因是因为我是个美工白痴所以图全是网上找的，抠图还是AI抠的（讲真的就这种美工水平还是埋了吧）

如果某一天技术力够的话说不定也可以渲染一下live2d模型（这一天还很远就是了）



欢迎新的开发者加入以及bug反馈

------

顺带一提，现在在和某位好基友一起整东方风格的stg引擎（C++写的）

------

**总之，祝各位使用愉快^_^**



