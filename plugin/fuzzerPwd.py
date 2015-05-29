#coding:gb2312
import os
import sys
from interface.iPlugin import Plugin
pwdlist=[]
sys.path.append('../')
wpath=os.path.dirname(__file__)
filepath=os.path.join(wpath,'file')
__all__ = ["fuzzerPwd"]
class fuzzerPwd(Plugin):
    """ ����һ���ӿڣ����� �������ʵ������ӿڣ�name ���Ա��븳ֵ """
    name = 'fuzzerPwd'
    description = 'һ��Fuzzer�������������'
    version = '0.0.1'
    
    def __init__(self):
        Plugin.__init__(self)
    
    #��ȡFuzzer�����ģ�壬ÿ��Ϊһ���Ž�pwdlist�б���
    def getPwdTemplat(self):
        fr=open(filepath+os.sep+'pwd.yx','r')
        while 1:
            line=fr.readline().strip()
            if not line:
                break
            pwdlist.append(line)

        fr.close()
    #��������ֵ�������ǰĿ¼�µ�password.txt�ļ�
    def outputDicFile(self,fuzzerPwdList):
        f=open(filepath+os.sep+'password.txt','w')
        for pwd in fuzzerPwdList:
           f.write(pwd+'\n')
        f.close()
    def execute(self,args):
        word=raw_input('������Fuzzer����Ĺؼ���[����ؼ���","����]:')
        wordlist=word.split(',')
        self.getPwdTemplat()
        '''
            �����б�������ģ��������滻Ϊ�б���Ĺؼ���
        '''
        fuzzerResult=[]
        for word in wordlist:
            for i in pwdlist:
                i=i.replace('%username%',word)
                if i not in fuzzerResult:
                    fuzzerResult.append(i)
        '''
            ����������Fuzzer��������
        '''
        for temp in fuzzerResult:
            print temp

        self.outputDicFile(fuzzerResult)
        return '����ѱ��浽'+filepath+os.sep+'password.txt��...'

