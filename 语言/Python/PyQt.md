```bash
pip install PyQt6
```

初始化

```python
app = QApplication()
```

控件

`QMainWindow`, `QPlainTextEdit`, `QPushButton` 是三个控件类，分别对应界面的主窗口，文本框和按钮，都是基于 `QWidget` 的子类。

```python
window = QMainWindow()
window.resize(500, 400)
window.move(300, 310)
window.setWindowTitle('Title')
```

