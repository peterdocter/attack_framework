# -*- coding:gb2312 -*-
__author__ = '����'
import os
import FrameworkPath
'''
    �����ļ�����
'''

def getPocFileList():
    uri=FrameworkPath.poc_dir
    return os.listdir(uri)
#��ʾpoc�ļ��б�
def showPocFileList():
    filelist=getPocFileList()
    print '*'*15+'��ѡ��exploitģ��'+'*'*15
    for pocfile in filelist:
        print '[*]'+pocfile


