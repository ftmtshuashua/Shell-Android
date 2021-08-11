# coding=utf-8
# APK 管理

import Phone

print('-------------- Start --------------')
# com.hunantv.market 还行-待观察
# 配置需要卸载的应用
_uninstall_packages = []
_uninstall_packages.append('com.tcl.qiyiguo')
_uninstall_packages.append('com.golive.cinema')  # - 删不掉
_uninstall_packages.append('cn.jmake.karaoke.box')
_uninstall_packages.append('com.xiaodianshi.tv.yst')
# _uninstall_packages.append('com.tcl.bootadservice') - 疑是开机广告
_uninstall_packages.append('com.mitv.tvhome.othertv')
_uninstall_packages.append('com.tcl.tshop')  # 电视购物
_uninstall_packages.append('com.iptv.ylhb')
_uninstall_packages.append('com.baosheng.ktv')
_uninstall_packages.append('com.tcl.vod')
_uninstall_packages.append('com.hunantv.market')
_uninstall_packages.append('com.tcl.weixin')
_uninstall_packages.append('com.tongyong.xxbox')
_uninstall_packages.append('com.huya.nftv')
_uninstall_packages.append('com.tcl.tliveplay')
_uninstall_packages.append('com.huanxi.tv')
_uninstall_packages.append('com.huan.edu.lexue.frontend')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')
_uninstall_packages.append('')

devices = Phone.getDevices()
if len(devices) != 1:
    print('请确保当前连接的设备有且之后一个!')
    exit()

device = devices[0]

print('当前设备：', device.getName())

packages = device.getPackages()
for package in packages:
    # print(package)
    intents = package.getIntentMainActivity()
    # print(intents)
    for intent in intents:
        intent.start()

print('-------------- Finish --------------')
