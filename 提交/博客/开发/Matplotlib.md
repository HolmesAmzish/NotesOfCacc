# Python Matplotlib

## 安装与设置

### 安装和使用

```bash
pip install matplotlib
```

只需要在程序开头导入相关库即可使用

```python
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()
```

<img src="../../../img/69.png" width=50%>

### 在程序中设置字体

在Matplotlib的默认设置中，通常无法显示中文或者负号，导致原本显示中文的地方只会显示一个空白正方形。所以需要手动设置字体。

可以在每个程序中主动设置当前的字体。以下代码就是设置字体为雅黑并将负号的显示改为一般ASCII码形式。

```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

### 全局设置

全局设置需要找到系统安装matplotlib的位置并找到配置文件，只需要进入python后查看即可。

```python
import matplotlib
print(matplotlib.matplotlib_fname())
```

随后就会显示对应的设置文件路径，例如

```
D:\Environment\Python312\Lib\site-packages\matplotlib\mpl-data\matplotlibrc
```

编辑这个路径的文件，需要找到以下行

```ini
# 设置字体
font.family: sans-serif
font.sans-serif: SimHei  # 使用黑体（可换成其他支持中文的字体）

# 设置负号
axes.unicode_minus: False
```



## 方法与成员

