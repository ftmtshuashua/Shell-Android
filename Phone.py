# coding=utf-8

import Utils


# 获得设备列表
def getDevices():
    popen = Utils.popen('adb devices')
    lines = popen.splitlines()
    _devices = []
    for line in lines[1:]:
        if line != '':
            _devices.append(Device(line))

    for device in _devices:
        print(device.getName(), device.getState())

    return _devices


# 定义Device数据结构
class Device:
    # 这个状态表示的是真机或者模拟器已经连接到了adb服务器上，但是并不代表我们已经可以对他们进行操作
    STATE_DEVICE = 'device'
    # 表示真机或者模拟器没有连接到adb 服务器 或者是没有响应。
    STATE_OFFLINE = 'offline'
    # 这个在我这里是没有显示的，直接是空。从字面就可以理解，没有找到有用的设备。
    STATE_NO_DEVICE = ''

    _NAME = None  # 设备名称
    _STATE = STATE_NO_DEVICE  # 设备状态

    def __init__(self, cmd_info):
        split = cmd_info.split('\t')
        self._NAME = split[0]
        self._STATE = split[len(split) - 1]
        pass

    def getName(self):
        return self._NAME

    def getState(self):
        return self._STATE


# 定义手机的数据结构
class Phone:
    def __init__(self, device):
        pass
