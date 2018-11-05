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
    f=open(latest_report, 'rb')
    mail_content=f.read()

    username = '348395870@qq.com'
    password = 'yksdwspckerkcacf'
    smtpServer = 'smtp.qq.com'

    sender = '348395870@qq.com'
    receiver = ['helloreverie@sina.com']
    subject='Test Report by Jazlnwang'

    message=MIMEText(mail_content,_subtype='html', _charset='utf-8')
    message['Subject'] = Header(subject,'utf-8')
    message['From'] = sender
    message['To'] = ','.join(receiver)

    try:
        smtp = smtplib.SMTP_SSL(smtpServer, 465)
        smtp.helo(smtpServer)
        smtp.ehlo(smtpServer)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, message.as_string())
    except:
        print('邮件发送失败')
    else:
        print('邮件发送成功')
        smtp.quit()
