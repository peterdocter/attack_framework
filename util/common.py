# -*- coding:gb2312 -*-
__author__ = '����'
import os
import re
'''
    ͨ�ò���
'''
#����post���󣬽�key=value����ʽת��Ϊ{key:value}���ֵ�����
def parseUrl(posturl):
    dict={}
    s=posturl.split('&')
    for re1 in s:
        dit=re1.split('=')
        dict[dit[0]]=dit[1]
    return dict
#����ƥ�䣬����ƥ�������б�
def regex(text,pattern):
    r=re.compile(pattern)
    result=r.findall(text)
    return result
#�ַ�����ӡģ��
def printPretty(str1):
    print '[*]'+'='*39
    print '[*]'+str1
    print '[*]'+'='*39