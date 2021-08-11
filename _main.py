# coding=utf-8
# 正式打包,并使用360加固后生成渠道包

import Android
import Utils

project_path = 'C:\hope\GiteeProject\WeatherApp'
app = Android.Project(project_path)

model = app.getModel('app')

print("ModelPath - ", model.getPath())
print("FilePath - ", model.getFilePath('\multidex-config.pro'))

bat = app.getFilePath("/_Resouce/shell/bat/")
#
# Utils.cmd(f'{bat}gradlew_clean.bat {app.getPath()}')
# Utils.cmd(f'{bat}gradlew_release.bat {app.getPath()}')
