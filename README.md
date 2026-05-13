# demo-ptyhon

> python学习记录

## 一、初始化配置
### 1. Python 安装 (Mac 版本)

#### 方式一：使用 Homebrew 安装（推荐）

```bash
# 1. 首先安装 Homebrew（如果未安装）
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. 安装 Python 3
brew install python@3.12
```

#### 方式二：官网下载安装包

1. 访问 [Python 官网](https://www.python.org/downloads/macos/)
2. 下载对应版本的安装包
3. 双击安装包，按提示完成安装

### 2. Python 多版本切换

#### 使用 pyenv 管理多版本（推荐）

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

### 3.安装PyCharm

#### 虚拟环境配置

##### 什么是虚拟环境？

虚拟环境是一个独立的 Python 运行环境，它可以：

- **隔离项目依赖**：不同项目使用不同版本的包，互不冲突
- **避免污染系统 Python**：不会在系统 Python 中安装大量第三方库
- **方便项目迁移**：可以轻松导出依赖列表，在其他机器上快速重建环境

举个例子：项目 A 需要 requests 2.25.1，项目 B 需要 requests 3.0.0，没有虚拟环境就会冲突。

---

##### 方式一：使用 venv（Python 内置，推荐）

```bash
# 1. 创建虚拟环境（在项目目录下执行）
python3 -m venv venv

# 2. 激活虚拟环境
# Mac/Linux:
source venv/bin/activate

# 激活成功后，命令行前面会有 (venv) 标识

# 3. 安装包
pip install requests
pip install pandas

# 4. 查看已安装的包
pip list

# 5. 导出依赖列表
pip freeze > requirements.txt

# 6. 退出虚拟环境
deactivate

# 7. 在新环境中重建依赖
pip install -r requirements.txt
```

---

##### 方式二：使用 Conda（适合数据科学）

```bash
# 1. 安装 Miniconda（如果未安装）
# 访问 https://docs.conda.io/en/latest/miniconda.html 下载安装

# 2. 创建虚拟环境
conda create -n myenv python=3.12

# 3. 激活环境
conda activate myenv

# 4. 安装包
conda install pandas
conda install numpy

# 或者使用 pip
pip install requests

# 5. 查看环境列表
conda env list

# 6. 导出环境
conda env export > environment.yml

# 7. 退出环境
conda deactivate

# 8. 从文件创建环境
conda env create -f environment.yml

# 9. 删除环境
conda remove -n myenv --all
```

