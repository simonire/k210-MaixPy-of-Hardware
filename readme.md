有关K210 MaixPy外设的所有代码

---K210 MaixPy of Hardware

​	---ssd1306

​	---servo

​	---...



# K210 MaixPy 新手使用指南

本指南说明的是 `MaixPy IDE` 开发环境，`Kendryte IDE` 不在本指南说明范围之内（指用C语言开发K210）



此文档适用于在【https://cn.maixpy.sipeed.com/zh】此处MaixPy文档阅读完看完迷糊的情况。

`MaixPy`全资料下载站【https://cn.dl.sipeed.com/MAIX】

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/M1_pin%5B1%5D.png)



> MaixPy 是将 [Micropython](http://micropython.org/) 移植到 [K210](https://kendryte.com/)（ 一款64位双核带硬件FPU和卷积加速器的 RISC-V CPU,  ） 的一个项目， 支持 MCU 常规操作， 更集成了机器视觉和麦克风阵列， 以快速开发具有极低成本和体积实用的 `AIOT` 领域智能应用。

> MicroPython 是基于 Python3 的语法做的一款解析器，包含了 Python3 的大多数基础语法， 主要运行在性能和内存有限的嵌入式芯片上。（注意 Micropython 不包含 Python3 的所有语法）
>
> K210 在硬件上集成了机器视觉和机器听觉能力， 是一款定位 AI 和 AIOT 市场的SoC，同时也是一颗方便的MCU。 

> Micropython 让我们在 K210 上编程更加简单快捷， 我们也将源代码开源在 [github](https://github.com/sipeed/MaixPy) 上

## 1 板子到手，查看基本信息

### - M1 / M1W

`Sipeed`  家的这四种开发板，其中除了BIT之外的三款，均采用  `M1/M1W`  核心模组：

<img src="https://cn.maixpy.sipeed.com/assets/M1_pin.png" alt="img" style="zoom:50%;" />

其中  `M1`  不带  ESP8285  ic，`M1W`  内置了 ESP8285 。

#### 1.  **Sipeed M1 (Lichee Dan) Dock Board**

<img src="https://cn.maixpy.sipeed.com/assets/Dan_Dock.png" alt="Dan dock" style="zoom:50%;" />

#### 2.  **Sipeed Maix Go**

<img src="https://cn.maixpy.sipeed.com/assets/Go.jpg" alt="Go" style="zoom:50%;" />

#### 3.  **Sipeed Maixduino**

<img src="http://spider.ws.126.net/1e8c74f7b0bff8465942c46fd43c88d3.jpeg" alt="img" style="zoom:50%;" />

​	Maixduino采用M1模组，并板载了一块ESP32模组用于与互联网连接。

#### 4.  **Sipeed Maix BiT**

<img src="https://cn.maixpy.sipeed.com/assets/BiT.png" alt="BiT" style="zoom:50%;" />

### - M1n  

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/20200410194244.png)

M1n采用的是M.2的金手指接口，通过对应的底座，可以将K210的引脚都引出到底板上，相比于M1/M1W模组，这种核心板更易于更换与维修。其核心板上板载了一个`24Pin FPC 前插后翻`接口的DVP摄像头。

## 2  烧录固件、下载、编程

​	

​	**新入手板子，请更新  固件版本 0.5.0.x 以上  和  ide版本0.2.4 以上**

​	**新入手板子，请更新  固件版本 0.5.0.x 以上  和  ide版本0.2.4 以上**

​	**新入手板子，请更新  固件版本 0.5.0.x 以上  和  ide版本0.2.4 以上**



#### 1. 准备一根TypeC线

很多人一上手就随便找了根TypeC，也不管里面到底有没有Rx和Tx，就问为什么会出现以下情况：

第一，	

要么烧录时出现下载不进，或者一上手就打开IDE运行代码的情况：

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/faq/1.png)

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/faq/2.png)

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/faq/3.png)

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/faq/4.png)



都建议买一根三四十的TypeC数据线，9.9包邮的你们敢用吗。。。

第二，

插上开发板如果不是显示以下的一种情况，就去打驱动：

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/a3.png)

或者

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/a4.png)



##### 对于 Dan Dock 和 Maix Bit

> 开发板使用了 `CH340` ：

##### 对于 Maix Go

> 开发板使用了一颗 `STM32` 来实现模拟串口以及 `JTAG`功能

> 这款 `STM32` 芯片的固件出厂默认采用 [open-ec](https://github.com/sipeed/open-ec) 的固件， 如果没问题，则会出现一个或者两个串口， 比如 `Linux` 下出现两个串口 `/dev/ttyUSB0` 和 `/dev/ttyUSB1`， 下载和访问串口时请使用 `/dev/ttyUSB1`。 Windows 也类似。

> 如果需要重新烧录这个固件，可以从 [github](https://github.com/sipeed/open-ec/releases) 或者 [官网下载 open-ec 固件](http://dl.sipeed.com/MAIX/tools/flash-zero.bin)， 然后使用 `ST-LINK` 连接板子上引出的 `STM32` 的 `SW` 引脚（`GND`, `SWDIO`, `SWCLK`）进行烧录。（目前版本的 `Go` 板子上的 `STM32` 不支持串口烧录，只能使用 `ST-LINK` 进行烧录， 有需要请自行购买，或者使用一款板子用 `IO` 模拟也可以（比如树莓派） ）

> 除了 `open-ec` 还有 `CMSIS-DAP` 固件， 相比 `open-ec` 可以模拟 `JTAG` 来对板子进行调试， `open-ec` 目前还未支持模拟 `JTAG`， 可以 [从官网下载固件](http://dl.sipeed.com/MAIX/tools/maix_go_cmsisdap_new.hex)， 使用 `ST-LINK` 对其进行烧录， 在 `Linux` 下会出现 `/dev/ttyACM0` 设备

#### 2. 下载固件、烧录软件：

烧录软件：https://github.com/sipeed/kflash_gui/releases

开发板固件：https://cn.dl.sipeed.com/MAIX/MaixPy/release/master  

按时间（**Modified**）排序，最靠前的点进去下载，这里以**maixpy_v0.5.0_36_gc3acf79**为例：

![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/a2.png)

其中，

```python
1 是最小固件，不带IDE支持，适用于烧录大模型文件，直接跑在板子上。
2 是最小固件，带IDE支持。
3 是完全固件，一般选择此项烧录。
4 是调试文件，不需留意，用于死机调试
5 是m5stickv开发板专用固件，一般用户不需使用。
6 是最大固件，支持IDE，并且LVGL支持的固件版本。
```

#### 3. 烧录固件：

- 打开 `kflash_gui` 应用
- 然后选择固件、设置选项， 点击下载即可

<img src="https://cn.maixpy.sipeed.com/assets/kflash_gui_screenshot_1.png" alt="img" style="zoom: 80%;" />

<img src="https://cn.maixpy.sipeed.com/assets/kflash_gui_screenshot_download.png" alt="img" style="zoom:80%;" />

#### 4 .MaixPy IDE

<img src="https://cn.maixpy.sipeed.com/zh/get_started/assets/helloworld-run.png" alt="helloworld-run.png" style="zoom:80%;" />

参考这段描述：【https://cn.maixpy.sipeed.com/zh/get_started/maixpyide.html】

## 3  MircoPython基础语法

参考这段描述：【https://docs.singtown.com/micropython/zh/latest/openmvcam/library/index.html】

## 4  使用MaixPy IDE



![](https://github.com/simonire/k210-MaixPy-of-Hardware/blob/master/img/a5.png)



仔细阅读此部分文档。

MaixPy历程：【https://github.com/sipeed/MaixPy_scripts】