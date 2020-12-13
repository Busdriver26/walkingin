# 安装Python3与依赖的教程

### 命令行：

本程序基于命令行工作，如果你不会命令行：

Windows: Win+R并在窗口输入cmd，再输入命令cd [main.py的路径]

MAC：打开“终端”

如：cd D:/folder1/folder2

运行：python main.py

#### 或者：

下载python的idle直接打开main.py-Run-Run module

### 0x00.python3:

如果你已经有Python3了，请留意是否多重安装了；如果多重安装了，请注意环境变量下的默认Python。

https://www.python.org/downloads/

你可以在上述页面根据你的操作系统下载对应的python3版本并安装。

### 0x01.依赖安装

打开你的python环境（如直接在命令行窗口输入Python,或者直接在你安装Python的地方双击python.exe）

```python
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
pip install pillow -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
pip install matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple/ 
```

