# -*- coding:gb2312 -*-
__author__ = '����'
import util.FileUtil as fileUtil
import lib.poc_core as pocCore
import argparse
import sys
import os
import lib.plugin_core as pluginCore


pluginObj=pluginCore.pluginCore()
def get_args():
    p=argparse.ArgumentParser()
    p.add_argument('-host',metavar='',help='ָ��Ŀ��������IP')
    p.add_argument('-exp',metavar='',help='ָ��һ��exploit����ģ��,�鿴exp�б�����exp=list')
    p.add_argument('-script',metavar='',help='ѡ��һ�����ʹ��,�鿴����б�����script=list')
    arguments=p.parse_args()
    return arguments
def parse_args():
    global pluginObj
    args=get_args()
    script=args.script
    exp=args.exp
    host=args.host
    if script=='list':
        pluginObj.showPluginList()
        print '[#]usage��'+os.path.basename(__file__)+' -script scriptName'
        sys.exit()
    if exp=='list':
        fileUtil.showPocFileList()
        print '[#]usage��'+os.path.basename(__file__)+' -host http://localhost/ -exp cmsexp.poc'
        sys.exit()
    if host!=None and exp!=None:
        executeExp(host,exp)
    if script!=None:
        use_script(script,host)

#�û�ѡ��ʹ�ò��
def use_script(scriptName,host=None):
    global pluginObj
    pluginObj.usePlugin(scriptName,host)
#ִ���û�ѡ���exp
def executeExp(host,pocfile):
    a=pocCore.Poc_Core(pocfile)
    a.attact(host)
if __name__ == '__main__':
    parse_args()