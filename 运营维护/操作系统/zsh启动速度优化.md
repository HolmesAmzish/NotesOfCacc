---
title: Zsh/Bash 启动速度优化
date: 2025-05-28
author: Cacciatore
---

# Zsh/Bash 启动速度优化

在安装完 Conda 之后，会发现每次启动 Zsh/Bash 的时候都需要加载时间，这个时候就会发现没有以前流畅了，原因是因为每次启动 Shell 时都需要去加载 Conda 环境，才能保证每次可以使用工具。然而官方自带的安装脚本在安装后都是强制每次启动 shell 时直接加载环境，会导致每次启动被拖慢，需要很多等待时间。本文提供**延迟启动**的方法，以提升每次的启动速度。

## 测试速度

首先需要分析是什么拖慢了启动时间，除了 Conda 作为主要拖慢启动的进程，可能还有其他。这里以 Zsh 为例，在启动脚本 `~/.zshrc` 开头中添加：

```bash
zmodload zsh/zprof
```

末尾添加：

```bash
zprof
```

最终可以看到输出，这里可以看到 nvm 和 conda 在 zsh 启动时占用了绝大部分时间。

```
num  calls                time                       self            name
-----------------------------------------------------------------------------------
 1)    2         291.99   146.00   48.89%    155.93    77.97   26.11%  nvm
 2)    1         114.14   114.14   19.11%    114.14   114.14   19.11%  compdump
 3)    1         118.46   118.46   19.83%    102.74   102.74   17.20%  nvm_ensure_version_installed
 4)    1         348.41   348.41   58.34%     56.42    56.42    9.45%  nvm_auto
 5)    1         199.97   199.97   33.48%     40.39    40.39    6.76%  compinit
 6)  815          37.68     0.05    6.31%     37.68     0.05    6.31%  compdef
 7)    1          15.71    15.71    2.63%     15.71    15.71    2.63%  nvm_is_version_installed
 8)    1          13.56    13.56    2.27%     13.56    13.56    2.27%  zrecompile
 9)    1          17.52    17.52    2.93%     12.53    12.53    2.10%  nvm_die_on_prefix
10)   22          14.00     0.64    2.34%     11.00     0.50    1.84%  _omz_source
11)    2           9.26     4.63    1.55%      9.26     4.63    1.55%  __sdkman_export_candidate_home
12)    2           8.36     4.18    1.40%      8.36     4.18    1.40%  compaudit
13)    2           5.98     2.99    1.00%      5.98     2.99    1.00%  __sdkman_prepend_candidate_to_path
14)    2           4.76     2.38    0.80%      4.76     2.38    0.80%  nvm_grep
15)    1           4.15     4.15    0.70%      4.15     4.15    0.70%  (anon)
16)    1           1.77     1.77    0.30%      1.77     1.77    0.30%  test-ls-args
17)    1           5.68     5.68    0.95%      1.53     1.53    0.26%  handle_update
18)    1           0.30     0.30    0.05%      0.30     0.30    0.05%  colors
19)    6           0.28     0.05    0.05%      0.28     0.05    0.05%  is-at-least
20)    4           4.99     1.25    0.84%      0.23     0.06    0.04%  nvm_npmrc_bad_news_bears
21)    4           0.14     0.04    0.02%      0.14     0.04    0.02%  add-zsh-hook
22)    3           0.12     0.04    0.02%      0.12     0.04    0.02%  bashcompinit
23)    2           0.18     0.09    0.03%      0.09     0.04    0.01%  complete
24)    1           0.08     0.08    0.01%      0.08     0.08    0.01%  nvm_has
25)    1         348.44   348.44   58.34%      0.03     0.03    0.01%  nvm_process_parameters
26)    3           0.03     0.01    0.00%      0.03     0.01    0.00%  is_theme
27)    2           0.02     0.01    0.00%      0.02     0.01    0.00%  is_plugin
28)    2           0.01     0.01    0.00%      0.01     0.01    0.00%  __sdkman_echo_debug
29)    1           0.01     0.01    0.00%      0.01     0.01    0.00%  nvm_is_zsh
30)    2           0.01     0.00    0.00%      0.01     0.00    0.00%  env_default

-----------------------------------------------------------------------------------

```



## 优化

将 Anaconda 和 NVM 设置成延迟启动，也就是只有在使用时加载环境，这样避免每次启动 zsh 就自动加载环境占用时间。

**Anaconda 加载**

```bash
# >>> conda initialize >>>
lazy_load_conda() {
  unalias conda 2>/dev/null
  
  # 初始化 conda
  __conda_setup="$('/home/cacc/anaconda3/bin/conda' 'shell.bash' 'hook' 2>/dev/null)"
  if [ $? -eq 0 ]; then
    eval "$__conda_setup"
  else
    if [ -f "/home/cacc/anaconda3/etc/profile.d/conda.sh" ]; then
      . "/home/cacc/anaconda3/etc/profile.d/conda.sh"
    else
      export PATH="/home/cacc/anaconda3/bin:$PATH"
    fi
  fi
  unset __conda_setup
  
  # 执行原命令
  conda "$@"
}
alias conda='lazy_load_conda'
# <<< conda initialize <<<
```

**Node Version Manager（NVM）加载**

```bash
# 延迟加载 NVM
export NVM_DIR="$HOME/.nvm"
lazy_load_nvm() {
  unalias nvm node npm yarn 2>/dev/null
  # 加载 nvm
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
  # 执行原命令
  "$@"
}
alias nvm='lazy_load_nvm nvm'
alias node='lazy_load_nvm node'
alias npm='lazy_load_nvm npm'
alias yarn='lazy_load_nvm yarn'
```

最后重新加载启动脚本：

```bash
source .zshrc
```

后面每次启动就只加载必要环境，启动时间大幅减小。