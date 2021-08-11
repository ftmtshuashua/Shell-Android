# coding=utf-8
# APK 管理

import os
import Phone


popen = os.popen('adb shell pm list package')
read = popen.read()
print(read)
popen.close()
