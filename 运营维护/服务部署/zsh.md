# 安装与配置 Zsh 的详细步骤

## **为什么选择 Zsh**

`bash` 是 Linux 系统默认的 Shell，功能强大且稳定，但其功能性和用户体验方面相对局限。对于日常开发、服务器维护甚至日常使用，`Zsh` 提供了以下优势：

- **插件支持**：Zsh 拥有丰富的插件生态系统，如 `git` 插件，可显示当前仓库状态。
- **主题丰富**：可以轻松更换命令行的外观，定制符合个人需求的主题。
- **命令补全**：更强大和智能的自动补全功能。
- **完全兼容 Bash**：即使切换到 Zsh，也无需担心兼容性问题。

## **安装 Zsh 和切换默认 Shell**

#### 1. 安装 Zsh

在 Ubuntu 或其他基于 Debian 的系统中：

```bash
sudo apt update
sudo apt install zsh -y
```

#### 2. 切换默认 Shell

```bash
chsh -s $(which zsh)
```

> **注意**：切换后需要注销或重新启动终端以使更改生效。

检查当前使用的 Shell：

```bash
echo $SHELL
```

如果输出是 `/usr/bin/zsh`，说明切换成功。

## **安装 Oh My Zsh**

`Oh My Zsh` 是一个强大的 Zsh 配置管理工具，支持主题和插件的快速安装。

#### 1. 在线安装

推荐通过 `curl` 或 `wget` 在线安装：

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

如果 GitHub 无法访问，可以使用国内镜像：

```bash
sh -c "$(curl -fsSL https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh)"
```

#### 2. 离线安装

如无法直接访问网络，使用以下步骤：

1. 在可以联网的设备上下载项目文件：

   ```bash
   git clone https://github.com/ohmyzsh/ohmyzsh.git
   tar -czvf oh-my-zsh.tar.gz ohmyzsh
   ```

2. 将 `oh-my-zsh.tar.gz` 传输到目标服务器（可使用 `scp`）。

3. 解压到用户目录：

   ```bash
   tar -zxvf oh-my-zsh.tar.gz -C ~/
   mv ~/ohmyzsh ~/.oh-my-zsh
   ```

4. 手动运行安装脚本：

   ```bash
   sh ~/.oh-my-zsh/tools/install.sh
   ```

## **配置 Zsh**

#### 1. 编辑 Zsh 配置文件

Oh My Zsh 的配置文件位于 `~/.zshrc`。打开编辑：

```bash
vim ~/.zshrc
```

将以下内容添加到配置文件中：

```ini
# 设置主题 (可以更换其他主题名称)
ZSH_THEME="agnoster"

# Oh My Zsh 安装路径
export ZSH="$HOME/.oh-my-zsh"

# 启用插件 (可以添加其他插件)
plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

# 加载 Oh My Zsh
source $ZSH/oh-my-zsh.sh

# 常用别名
alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

# 添加 PATH
export PATH="$HOME/bin:/usr/local/bin:$PATH"

# 自定义命令提示符
autoload -U promptinit; promptinit
prompt agnoster
```

对于想要更改主题的，可以参考官方网站：https://github.com/ohmyzsh/ohmyzsh/wiki/Themes

#### 2. 安装插件

1. **自动建议插件 (zsh-autosuggestions)**：

   ```bash
   git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions
   ```

   启用方法：将 `zsh-autosuggestions` 添加到 `plugins=(...)` 中。

2. **语法高亮插件 (zsh-syntax-highlighting)**：

   ```bash
   git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting
   ```

   启用方法：同上。

3. **Powerlevel10k 主题 (可选)**： Powerlevel10k 是一个现代的 Zsh 主题，性能极高，支持高度自定义。

   ```bash
   git clone https://github.com/romkatv/powerlevel10k.git ~/.oh-my-zsh/custom/themes/powerlevel10k
   ```

   启用方法：将 `ZSH_THEME="powerlevel10k/powerlevel10k"` 添加到 `~/.zshrc` 中。

#### 3. 重载配置

保存更改后，执行以下命令重新加载：

```bash
source ~/.zshrc
```

