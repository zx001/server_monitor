#!/usr/bin/env python3
#coding: utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import sys
import os
import re
import time

def send_mail(userdRate):
        sender = 'sender'
        receiver = 'receiver'
        smtpserver = 'smtpserver'
        username = 'username'
        password = 'password'
        filePathStatus = os.popen("cat /proc/meminfo").readlines()
        tempHtmlTxt = '<br/>/proc/meminfo：<br/>'
        for t in filePathStatus:
                tempHtmlTxt = tempHtmlTxt + t.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;").replace("\n", "<br/>")
        msgRoot = MIMEMultipart('related')
        msgRoot['to'] = receiver
        msgRoot['from'] = sender
        msgRoot['Subject'] = '【紧急】xxx 服务器内存剩余空间不足，目前空闲内存' + str(userdRate) + 'KB'
        msgText = MIMEText('服务器内存已满，请及时清理，<br/>内存使用情况如下：' + '<br/>' + tempHtmlTxt, 'html', 'utf-8')
        msgRoot.attach(msgText)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()

def main():
        while(1):
                memoryStatus = os.popen("cat /proc/meminfo | grep MemFree").readlines()[0]
                memFree = int(re.sub(r'\s+', " ", memoryStatus).split(" ")[1])
                if(memFree <= 5242880):
                        send_mail(memFree)
                time.sleep(3600)

if __name__ == '__main__':
        main()

