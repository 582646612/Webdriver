#coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
import logging

#获取最新测试报告
def latest_report(report_dir):
    lists=os.listdir(report_dir)
    lists.sort(key=lambda fn:os.path.getatime(report_dir+'//'+fn))
    logging.info('the latest report is :' +lists[-1])
    file=os.path.join(report_dir,lists[-1])
    return file


#发送邮件
def sendEmail(latest_report):
    with open(latest_report, 'r') as f:
       mail_content=f.read()

    sender = 'cs825096095@163.com'
    receiver = "825096095@qq.com"
    subject = 'python email test'
    smtpServer = 'smtp.163.com'
    username = 'cs825096095@163.com'
    password = 'cs123456'

    message=MIMEText(mail_content,_subtype='html', _charset='utf-8')
    message['From'] = sender
    message['To'] = receiver
    subject = '测试标题'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpServer, 25)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
    except:
        print('邮件发送失败')
    else:
        print('邮件发送成功')
        smtp.quit()
if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.dirname(__file__))
    report_dir = base_dir + "/reports"
    sendEmail(latest_report(report_dir))