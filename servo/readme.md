`Servos`方法类里面有四个方法：

```c
def set(angle)
```

此方法传入一个角度值，范围在-90 ~ 90之间。

```c
def setting_degree(func ,angle)
```

此方法传入一个`func`变量和角度值来设定open()方法和close()方法的角度值

```c
def open()  
```

驱动舵机打开，无需传入值。

```c
def close()
```

驱动舵机关闭，无需传入值。