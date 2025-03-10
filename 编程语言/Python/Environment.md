---
title: Python 的环境
date: 2025-02-03 22:48
tags: ['python']
---

# pip

**`pip`** 是 Python 的标准包管理工具，用于安装和管理 Python 软件包。它允许你从 Python 包索引（PyPI）下载并安装第三方库，并能自动解决依赖问题。

## 第三方库的安装与卸载

```bash
pip install <package>

pip uninstall <package>
```

`pip` 还支持安装指定版本的包：

```bash
pip install <package>==<version>

pip install requests==2.24.0
```

更新包：

```bash
pip install --upgrade <package-name>
```



## 查看

当前环境安装的列表

```bash
pip list
```

查看某个特定的包是否安装

```bash
pip show <package_name>
```

将当前环境安装的包输出到 `requirements.txt` 文件中

```bash
# 输出第三方库环境
pip freeze > requirements.txt

# 安装指定环境
pip install -r requirements.txt
```





# Venv

venv 是 Python 3.3 及以上版本自带的虚拟环境管理工具，用于创建和管理隔离的 Python 环境。其提供了一种简单的方法确保项目依赖与系统环境和其他项目的依赖隔离开来避免冲突

## Venv 环境的管理

一般创建 venv 虚拟环境是为每个项目单独创建，PyCharm 一般会自动为项目创建虚拟环境，文件都列在项目根目录的 `.venv` 文件夹中。

要手动创建虚拟环境，可以在项目根目录输入以下指令，创建一个 `.venv` 文件夹。一般前缀带 `.` 会被自动隐藏。

```bash
python -m venv .venv
```

激活环境

```cmd
# Windows
.venv\Scripst\activate
```

```bash
# Linux
source .venv/bin/activate
```

## 第三方库的管理

venv 一般直接使用 `pip` 进行下载，激活虚拟环境后，`PATH` 等路径变量都被更改，此时使用 pip 对库进行更改都会更改当前虚拟环境。

下载包

```bash
pip install <package>
```



# Anaconda

**Anaconda** 是一个开源的 Python 和 R 编程语言的发行版，主要用于数据科学、机器学习、人工智能和科学计算等领域。Anaconda 提供了独立环境并为项目使用。也就是多个项目如果背景一样可以使用同一个由conda管理的环境。

## Conda 环境的管理

列出所有环境

```bash
conda env list # List all environments
```

创建环境

```bash
conda create --name <env_name> (python=<python_version>)
```

删除环境

```bash
conda env remove --name <env_name>
```



禁用终端自动初始化

```bash
conda config --set auto_activate_base false
```





## 环境的激活

```bash
conda activate <env>
conda deactivate
```



## 第三方库的管理

```bash
conda install <package>
conda install notebook numpy scikit-learn pandas matplotlib scipy opencv-python xgboost flask spacy plotly onnx onnxruntime


conda uninstall <package>
```



# Mniconda

**Miniconda** 是 **Anaconda** 的一个轻量级替代品。它是一个小型的包管理工具和环境管理系统，主要由 **`conda`** 包管理器和最小化的 Python 环境组成。与 Anaconda 不同，Miniconda 不预装大量的科学计算包，而是提供一个简洁的基础环境，用户可以根据自己的需求安装所需的包和工具。

以树莓派安装 Mniconda 为例：

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh

chmod +x Miniconda3-latest-Linux-armv7l.sh
./Miniconda3-latest-Linux-armv7l.sh

conda init
source ~/.bashrc
```

