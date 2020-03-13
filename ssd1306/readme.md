之前优惠的时候在得捷下单买了块DFROBOT的oled屏幕，一直没来得及用上，这下寒假疫情在家，终于有空来试试K210+ssd1306。

HELLO.py
```
import time
from ssd1306 import Oled

oled96 = Oled(20,21)
oled96.oled_showstr(0,3,">Python is cool.")

```

其中`scl`和`sda`可以根据原理图进行指定注册，只要是k210（我用的是m1n）在硬件图上没有用到的引脚，都可以使用。当然也可以用

```
import os
os.listdir()
```
来查看引脚布局图。

SSD1306.py

```
    def __init__(self,scl,sda):
    def oled_init(self):
    def oled_on(self):
    def oled_off(self):
    def oled_setpixel(self,x,y):
    def oled_clear(self):
    def oled_full(self):
    def oled_showstr(self,x,y,data):
    def oled_lessismore(self):
    def oled_talkfirst(self):

```
要在ssd1306上显示字符就调用`oled96.oled_showstr(x,y,data)`这个方法。 x，y取值在0-7之间，data是字符串类型。

另外，在库里提供了两个显示方法`oled_lessismore()`,`oled_talkfirst()`,具体内容
```
    def oled_lessismore(self):
        self.oled_showstr(0,2, " Python is Hard ")
        self.oled_showstr(0,4, "    Let it Go   ")
    def oled_talkfirst(self):
        self.oled_showstr(0,2, " Python is Good ")
        self.oled_showstr(0,4, "    Do it now   ")
```

连接上Maix，选择发送文件到开发板，选择`SSD1306.py`

![a1](F:\GitHub project\K210 MaixPy of Hardware\ssd1306\pic\a1.png)

之后新建一个`hello.py`

![a2](F:\GitHub project\K210 MaixPy of Hardware\ssd1306\pic\a2.png)

![a3](F:\GitHub project\K210 MaixPy of Hardware\ssd1306\pic\a3.png)

就可以显示了。

![a4](F:\GitHub project\K210 MaixPy of Hardware\ssd1306\pic\a4.JPG)