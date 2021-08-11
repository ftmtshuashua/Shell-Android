# coding=utf-8

import os
import re

import Utils


# Android工程
class Project:
    _PATH = None  # 工程地址
    _MODELS = {}  # 工程种的Model

    #project_path:Android项目的根目录地址
    def __init__(self, project_path):
        self._PATH = Utils.getAbsPath(project_path)  # 工程目录
        print('解析项目:', self._PATH)
        self._parse()

    # 解析工程
    def _parse(self):
        self._MODELS.clear()
        for line in open(f'{self._PATH}{Utils.SEPARATOR}settings.gradle', 'rt', encoding='UTF-8'):
            if re.search('^include +(\'|\"):.*(\'|\")$', line):
                self._parse_Model(re.findall("[\w|\-|~|!|@|#|$|%|^|&|*|(|)]*", line)[4])

    # 解析Model
    def _parse_Model(self, model):
        model_path = f'{self._PATH}\{model}'
        if os.path.exists(model_path):
            self._MODELS[model] = Model(model_path)

    # 获得Model对象
    def getModel(self, name):
        return self._MODELS[name]

    def toString(self):
        print("Project:", self._PATH)
        print("Models:", self._MODELS)

    def getPath(self):
        return self._PATH

    # 获得项目中的文件地址
    # file : app/build.gradle
    def getFilePath(self, file):
        return self._PATH + file


# Android Model
class Model:
    # Model文件夹地址
    _PATH = None
    # 文件夹名字
    _NAME = None
    # Model类型 com.android.application | com.android.library
    _MODEL_TYPE = {}

    def __init__(self, path):
        self._PATH = path
        self._NAME = Utils.getFileName(path)
        self._parse()

        print('发现Model:', self._NAME, f'({self._plugin_()})')
        pass

    def _parse(self):
        # Model类型解析
        path = f'{self._PATH}{Utils.SEPARATOR}build.gradle'
        file = open(path, 'rt', encoding='UTF-8')
        text = file.read()
        self._MODEL_TYPE['com.android.library'] = text.__contains__('com.android.library')
        self._MODEL_TYPE['com.android.application'] = text.__contains__('com.android.application')
        self._MODEL_TYPE['kotlin-android'] = text.__contains__('kotlin-android')
        pass

    # Model的插件信息
    def _plugin_(self):
        array = []
        if self.isApplication():
            array.append("App")
        if self.isLibrary():
            array.append("Lib")
        if self.isKotlin():
            array.append("Kotlin")
        return ','.join(array)

    def isApplication(self):
        return self._MODEL_TYPE['com.android.application']

    def isLibrary(self):
        return self._MODEL_TYPE['com.android.library']

    def isKotlin(self):
        return self._MODEL_TYPE['kotlin-android']

    # 获得Model的路径
    def getPath(self):
        return self._PATH

    # 获得Model的名称
    def getName(self):
        return self._NAME


    def getFilePath(self, file):
        return self.getPath() + file
