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
        filePathStatus = os.popen("du -sh [your path]").readlines()
        tempHtmlTxt = '<br/>所占空间&nbsp;&nbsp;&nbsp;&nbsp;路径<br/>'
        for t in filePathStatus:
                tempHtmlTxt = tempHtmlTxt + t.replace("\t", "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;").replace("\n", "<br/>")
        msgRoot = MIMEMultipart('related')
        msgRoot['to'] = receiver
        msgRoot['from'] = sender
        msgRoot['Subject'] = '【紧急】xxx 服务器磁盘剩余空间不足，目前已占用' + userdRate
        msgText = MIMEText('服务器磁盘已满，请及时清理，<br/>[your path]路径详细情况如下：' + '<br/>' + tempHtmlTxt, 'html', 'utf-8')
        msgRoot.attach(msgText)
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()

def main():
        while(1):
                filesystemStatus = os.popen("df -h | grep /dev/vda1").readlines()[0]
                userdRate = re.sub(r'\s+', " ", filesystemStatus).split(" ")[4]
                userdValue = int(userdRate.replace('%', ''))
                if(userdValue >= 80):
                        send_mail(userdRate)
                time.sleep(3600)

if __name__ == '__main__':
        main()

