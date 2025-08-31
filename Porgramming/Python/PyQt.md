```bash
pip install PyQt6
```

## 第一个程序

首先导入必要的包，基础小组件位于 `PyQt6.QWidgets` 模块。

```python
# file: simple.py

"""
A simple program for PyQt
Date: 2025-01-27
Author: Holmes Amzish
"""


import sys
from PyQt6.QtWidgets import QApplication, QWidget


def main():
    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(800, 600)
    # window.move(300, 300)
    window.setWindowTitle('Simple')

    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
```



初始化，其中 `QApplication` 提供了整个图形化界面程序的底层管理功能。`sys.argv` 参数是来自命令行的

```python
app = QApplication(sys.argv)
```





控件

`QMainWindow`, `QPlainTextEdit`, `QPushButton` 是三个控件类，分别对应界面的主窗口，文本框和按钮，都是基于 `QWidget` 的子类。





### QMainWindow

> [!TIP]
>
> `QMainWindow` 是专门为应用程序主窗口设计的类，提供了一些标准的主窗口功能，比如菜单栏，工具栏和状态栏以及中心窗口部件。
>
> 而 `QWidget` 是 Qt 所有 UI 组件的基类，可以作为一个普通窗口。



```python
window = QMainWindow() # 创建主窗口对象
window.resize(500, 400)
window.move(300, 310) # 启动后的位置
window.setWindowTitle('Title')
```

### QPlainTextEdit

`QPlainTextEdit` 是一个文本框类。

```python
textEdit = QPlainTextEdit(window)
textEdit.setPlaceholderText("Input text...")
textEdit.move(10,25) # 在父级窗口的位置
textEdit.resize(300,350)
```



最后通过 QMainWindow 的 show 方法展示

```python
window.show()

app.exec() # 等待用户响应
```

# 信号与插槽

基于 GUI 的应用程序是事件驱动的，函数或方法响应用户的操作，例如单击按钮和从集合中选择项目或单机鼠标等执行，称为 events。而用于构建 GUI 界面的小部件充当此类事件的来源。每个派生于 QObject 类的 PyQt 小部件都旨在发出信号（Signal）以响应一个活多个事件，信号需要连接到插槽，而插槽可以是任何可调用的 Python 函数。
