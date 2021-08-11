# coding=utf-8

import re

import Utils


# 获得设备列表
def getDevices():
    popen = Utils.popen('adb devices')
    lines = popen.splitlines()
    _devices = []
    for line in lines[1:]:
        if line != '':
            _devices.append(Device(line))

    # for device in _devices:
    #     print(device.getName(), device.getState())

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

    def getPackages(self):
        _popen = Utils.popen('adb shell pm list package')
        _lines = _popen.splitlines()
        # print(_lines)
        _Packages = []
        for str in _lines:
            if str != '':
                _Packages.append(Package(str))
        return _Packages


class Package:
    _package_name = None
    _intent_main_activity = []

    def __init__(self, package: str):
        _split = package.split(':')
        # print(_split)
        self._package_name = _split[1]
        self._parse_main_activity()

    def _parse_main_activity(self):
        _popen = Utils.popen(f'adb shell dumpsys package {self._package_name}')
        _splitlines = _popen.splitlines()
        _splitlines = Utils.removeNull(_splitlines)
        # print(_splitlines)

        _intents = []

        for index, action in enumerate(_splitlines):
            if action.__contains__('android.intent.action.MAIN'):
                _index = index + 1
                # print(_str_line)
                # print(re.search(f'^        [0-9a-zA-Z]+ .*$', _str_line))
                # while self._isIntent(_str_line):
                while re.search(f'^        [0-9a-zA-Z]+ .*$', _splitlines[_index]) is not None:
                    _intent = self._getIntent(self._package_name, _splitlines[_index])
                    _intents.append(Intent(_intent))
                    _index += 1
                    continue
                break
        self._intent_main_activity = _intents
        # print(self._intent_main_activity)
        pass

    # 获得Intent字符串
    @staticmethod
    def _getIntent(package, _intents):
        return re.findall(f'{package}/[0-9a-zA-Z.]*', _intents)[0]

    # 判断是否为Intent
    @staticmethod
    def _isIntent(_intents):
        return re.search(f'^        [0-9a-zA-Z]{8} .*$', _intents)

    def getIntentMainActivity(self):
        return self._intent_main_activity


# Intent
class Intent:
    _intent = None

    def __init__(self, _intent):
        # print(_intent)
        self._intent = _intent

    # 启动命令
    def start(self):
        # adb shell am start -n com.tcl.factory.view/.MainMenu  开发者设置

        msg = self.getmsg(self._intent)
        if msg == '':
            print(f'adb shell am start -n {self._intent}')
        else:
            print(f'adb shell am start -n {self._intent}    - {msg}')

    def getmsg(self, intent):
        if intent == 'com.tcl.factory.view/.MainMenu': return '开发者工具'
        if intent == 'com.tcl.tvhealthcheck/.MainActivity': return '体检系统'
        if intent == 'com.tcl.screensaver/.MainActivity': return '屏保'
        if intent == 'com.tcl.browser/.SiteMapActivity': return '牛逼浏览器'
        if intent == 'com.tcl.SmartTVHelp/.HomeActivity': return '帮助中心'
        if intent == 'com.tcl.MultiScreenInteraction_TV/.SplashActivity': return '多屏互动'
        if intent == 'com.tcl.tliveplay/.activitys.MainActivity': return '网络直播'
        if intent == 'com.tcl.tvweishi/.activity.StartActivity': return '电视卫视'
        if intent == '': return ''
        if intent == '': return ''
        if intent == '': return ''
        if intent == '': return ''
        if intent == '': return ''

        return ''
