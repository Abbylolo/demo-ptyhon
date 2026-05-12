# demo-ptyhon

> python学习记录

## 1. Python 安装 (Mac 版本)

### 方式一：使用 Homebrew 安装（推荐）

```bash
# 1. 首先安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安装 Python 3
brew install python@3.12
```

### 方式二：官网下载安装包

1. 访问 [Python 官网](https://www.python.org/downloads/macos/)
2. 下载对应版本的安装包
3. 双击安装包，按提示完成安装

## 2. Python 多版本切换

### 使用 pyenv 管理多版本（推荐）

```bash
# 1. 安装 pyenv
brew install pyenv

# 2. 配置 shell（根据你使用的 shell 选择）
# 对于 zsh (Mac 默认):
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

source ~/.zshrc

# 对于 bash:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

source ~/.bash_profile

# 3. 查看可安装的 Python 版本
pyenv install --list

# 4. 安装特定版本
pyenv install 3.9.19
pyenv install 3.10.14
pyenv install 3.11.9
pyenv install 3.12.4

# 5. 查看已安装版本
pyenv versions

# 6. 设置全局 Python 版本
pyenv global 3.12.4

# 7. 设置当前目录 Python 版本
pyenv local 3.10.14

# 8. 切换到系统 Python
pyenv global system

# 9. 查看当前使用 Python 版本
python3 --version 或 python3 -V
```

