# coding=utf-8

import inspect
import os

# 当前脚本文件所在的目录
PATH_SHELL_ROOT_DIR = os.getcwd()
# 当前文件的绝对路径
PATH_FILE = inspect.getfile(inspect.currentframe())
# 目录的分隔符
SEPARATOR = '\\'


# 文件重命名
# old_name : 旧目录/文件名的绝对路径
# new_name : 新文件/文件名的绝对路径
def rename(file, new_name):
    if not os.path.exists(file):
        raise Exception(f'{file} 文件不存在!')
    _dir = getFileDir(file)
    _join_old = os.path.join(_dir, getFileName(file))
    _join_new = os.path.join(_dir, new_name)
    os.rename(_join_old, _join_new)


# 设置文件前缀
# file: 文件名
# prefix: 给文件增加的前缀
def setPrefix(file, prefix):
    if os.path.isfile(file) | os.path.isdir(file):
        rename(file, f'{prefix}{getFileName(file)}')
    else:
        raise Exception(f'{file} 不是一个文件!')


# 判断文件前缀是否为传入值
def isPrefix(file, prefix):
    if os.path.isfile(file):
        name = getFileName(file)
        return name.startswith(prefix)
    else:
        return file.startswith(prefix)


# 获得文件所在目录
def getFileDir(file):
    if os.path.isdir(file):
        return os.path.dirname(file)
    if os.path.isfile(file):
        return os.path.dirname(file)
    raise Exception(f'{file} : 获取目录失败')


# 获得文件名
def getFileName(file):
    return os.path.basename(file)
    raise Exception(f'{file} : 文件名解析错误!')


# 获得绝对路径
def getAbsPath(file):
    return os.path.abspath(file)


# 执行CMD命令
def cmd(cmd):
    print('CMD:', cmd)
    os.system(cmd)


# 查找工程跟目录 - 如果该文件在Android项目内
def getAndroidRootDir():
    _dir = PATH_SHELL_ROOT_DIR
    while True:
        _isAP = _isAndroidProject(_dir)
        if _isAP: return _dir
        _old = _dir
        _dir = getFileDir(_dir)
        if _dir == _old: return None


# 判断是否为Android项目
def _isAndroidProject(dir):
    for _str in ['settings.gradle', 'gradlew.bat', 'gradle.properties', 'build.gradle', 'settings.gradle']:
        if not os.path.exists(f'{dir}{SEPARATOR}{_str}'): return False
    return True
