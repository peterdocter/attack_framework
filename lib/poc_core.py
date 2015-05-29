# -*- coding:gb2312 -*-
__author__ = '����'
import ConfigParser
import FrameworkPath
import os
import requests
import util.common as common
from time import sleep
class Poc_Core:
    def __init__(self,pocFile):
        self.pocFile=pocFile
    #����poc�ļ�
    def parsePoc(self):
        try:
            cf=ConfigParser.ConfigParser()
            cf.read(FrameworkPath.poc_dir+os.sep+self.pocFile)
            items=cf.items("exploit")
            pocpath=items[0][1]
            payload=items[1][1]
            res_match=items[2][1]
            requestMethod=items[3][1]
            return pocpath,payload,res_match,requestMethod
        except Exception,e:
            print '����poc�ļ�ʧ�ܣ���ȷ�������Ƿ�淶:%s'%(e)
    #ͨ��������poc�ͷ�������ȥִ�й�������
    def attact(self,url):

        pocpath,payload,res_match,requestMethod=self.parsePoc()
        requestMethod=requestMethod.lower().strip()
        if requestMethod=='post':
            postdata=common.parseUrl(payload)
            r=requests.post(url+'/'+pocpath,data=postdata)
            if r.status_code==200:
                m=common.regex(r.content,res_match)
                if m:
                    for resut in m:
                        common.printPretty('result:'+resut)
                else:
                    common.printPretty('�������ץȡʧ��...����ӡ���з�������...')
                    sleep(1)
                    common.printPretty(r.content)
        elif requestMethod=='get':
            r=requests.get(url+'/'+pocpath+payload)
            if r.status_code==200:
                m=common.regex(r.content,res_match)
                if m:
                    for resut in m:
                        common.printPretty('result:'+resut)
                else:
                    common.printPretty('�������ץȡʧ��...����ӡ���з�������...')
                    sleep(1)
                    common.printPretty(r.content)

