# -*- coding:gb2312 -*-
__author__ = '����'
from util.pluginManager import DirectoryPluginManager
from time import sleep
import os
#��ʾ���в����Ϣ
class pluginCore:
    def __init__(self):
        self.plugin_manager = DirectoryPluginManager()
        self.plugin_manager.loadPlugins()
    def usePlugin(self,pname,host=None):
        plugins = self.plugin_manager.getPlugin(pname)
        print 'start'+('=='*24)+'==>'
        sleep(1)
        if host==None:
            print plugins.execute(None)
        elif host!=None:
            print plugins.execute(host)
    def showPluginList(self):
        print '<'+('='*20)+'exploit list��'+('='*20)+'>'
        self.plugin_manager.showPluginList()