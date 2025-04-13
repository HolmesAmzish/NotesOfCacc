---
title: Python 的环境
date: 2025-02-03 22:48
tags: ['python']
---

# Python 环境管理工具

在 Python 开发过程中，环境管理是确保项目依赖不冲突的关键。使用适当的工具可以帮助你轻松管理不同项目的依赖，保持系统清洁，并提高开发效率。常用的 Python 环境管理工具包括 `pip`、`venv`、`Anaconda` 和 `Miniconda`。

## 1. **pip：Python 包管理器**

**`pip`** 是 Python 的官方包管理工具，用于安装、更新和卸载 Python 软件包。

### 安装与卸载第三方库

```bash
# 安装库
pip install <package>

# 卸载库
pip uninstall <package>
```

### 安装指定版本的包

```bash
# 安装指定版本
pip install <package>==<version>

# 示例
pip install requests==2.24.0
```

### 更新库

```bash
pip install --upgrade <package-name>
```

### 查看已安装的库

```bash
# 查看当前环境已安装的库列表
pip list

# 查看某个特定包的详细信息
pip show <package_name>
```

### 导出与安装依赖

- 将当前环境安装的库输出到 `requirements.txt` 文件：

```bash
pip freeze > requirements.txt
```

- 从 `requirements.txt` 安装依赖：

```bash
pip install -r requirements.txt
```

`requirements.txt` 文件通常包含项目所需的所有包和版本信息，方便团队共享和环境复现。

------

## 2. **venv：虚拟环境管理**

`venv` 是 Python 3.3 及以上版本自带的虚拟环境工具，允许你为每个项目创建独立的环境，从而隔离项目的依赖，避免不同项目间的库冲突。

### 创建虚拟环境

在项目根目录下创建虚拟环境：

```bash
python -m venv .venv
```

默认情况下，`venv` 会在当前目录下创建一个名为 `.venv` 的文件夹，包含 Python 解释器和包管理工具。

### 激活虚拟环境

- **Windows**:

```bash
.venv\Scripts\activate
```

- **Linux/macOS**:

```bash
source .venv/bin/activate
```

激活虚拟环境后，你的命令行提示符会发生变化，表明你已进入虚拟环境。

### 使用 `pip` 安装包

在激活虚拟环境后，所有通过 `pip` 安装的库都会被安装到该环境中：

```bash
pip install <package>
```

### 退出虚拟环境

退出虚拟环境时，运行：

```bash
deactivate
```

------

## 3. **Anaconda：Python 数据科学发行版**

**Anaconda** 是一个开源的 Python 和 R 编程语言的发行版，专为数据科学、机器学习、人工智能和科学计算设计。Anaconda 提供了包管理和环境管理的功能，尤其适用于处理大量数据分析任务和科学计算。

### Anaconda 与 Conda

**Conda** 是 Anaconda 提供的包管理器和环境管理器，允许你管理 Python 环境和其他依赖包。

### 创建环境

创建一个新的 Conda 环境时，可以指定 Python 版本：

```bash
conda create --name <env_name> python=<python_version>
# 示例：创建一个名为 "ml_env" 的 Python 3.9 环境
conda create --name ml_env python=3.9
```

### 激活与退出环境

```bash
# 激活环境
conda activate <env_name>

# 退出环境
conda deactivate
```

### 查看环境

列出所有 Conda 环境：

```bash
conda env list
```

### 安装与卸载包

```bash
# 安装包
conda install <package>

# 卸载包
conda uninstall <package>
```

### 更新 Conda 和包

```bash
# 更新 Conda
conda update conda

# 更新包
conda update <package>
```

### 配置 Conda 自动激活

默认情况下，Anaconda 会在每次终端启动时自动激活 `base` 环境。你可以禁用此功能：

```bash
conda config --set auto_activate_base false
```

------

## 4. **Miniconda：轻量版 Anaconda**

**Miniconda** 是 Anaconda 的一个轻量级版本，仅包含 Conda 包管理器和 Python 环境，而不预装大量的科学计算库。它提供了更简洁的基础环境，适合用户根据需要安装所需的库和工具。

### 安装 Miniconda

以树莓派为例，安装 Miniconda 的步骤：

```bash
# 下载 Miniconda 安装脚本
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh

# 赋予执行权限并运行安装
chmod +x Miniconda3-latest-Linux-armv7l.sh
./Miniconda3-latest-Linux-armv7l.sh

# 初始化 conda
conda init

# 激活修改
source ~/.bashrc
```

Miniconda 安装后，你可以按需安装和管理所需的库，而不会浪费存储空间。

------

## 5. **对比：pip、venv、Anaconda 与 Miniconda**

| 特性         | pip                         | venv                     | Anaconda                     | Miniconda                    |
| ------------ | --------------------------- | ------------------------ | ---------------------------- | ---------------------------- |
| **用途**     | 包管理工具                  | 虚拟环境管理工具         | 环境与包管理工具             | 轻量级环境与包管理工具       |
| **管理方式** | 仅通过包安装与卸载          | 创建隔离的 Python 环境   | 使用 Conda 管理环境与包      | 使用 Conda 管理环境与包      |
| **包来源**   | PyPI                        | 通过 pip 从 PyPI 安装    | Conda 仓库                   | Conda 仓库                   |
| **环境管理** | 通过 `virtualenv` 或 `venv` | 通过 `venv` 创建虚拟环境 | 提供虚拟环境管理功能         | 提供虚拟环境管理功能         |
| **包缓存**   | 无缓存机制                  | 无缓存机制               | Conda 缓存机制               | Conda 缓存机制               |
| **适用场景** | 简单的 Python 项目          | 项目隔离，解决依赖冲突   | 数据科学、机器学习、科学计算 | 数据科学、机器学习、科学计算 |

------

## 6. **总结**

- **pip** 是 Python 的官方包管理工具，适合用于简单的包管理。
- **venv** 是 Python 自带的虚拟环境工具，能够为每个项目创建隔离的环境，防止依赖冲突。
- **Anaconda** 和 **Miniconda** 提供了更强大的环境与包管理功能，适合用于数据科学和机器学习项目。
- **Miniconda** 是 Anaconda 的轻量级版本，适合需要定制化环境的用户。
