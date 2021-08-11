# coding=utf-8
# APK 管理

import Phone

devices = Phone.getDevices()
if len(devices) != 1:
    print('请确保当前连接的设备有且之后一个!')
    exit()


# popen = os.popen('adb shell pm list package')
# read = popen.read()
# print(read)
# popen.close()
