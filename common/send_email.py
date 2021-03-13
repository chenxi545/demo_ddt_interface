from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email_text():
    # 第一步连接smtp服务
    s = smtplib.SMTP()
    # 注意163端口25，qq邮箱端口是465
    s.connect(host='smtp.126.com', port=25)

    # 第二步登录到stmp服务器
    user = 'm16639931390@126.com'
    pwd = 'BVYDHHUQPEJLDLBF'
    s.login(user=user, password=pwd)

    # 第三步发送邮件
    # 构造邮件正文
    content = '这个是用来测试的邮件，看看能不能发成功！'
    msg = MIMEText(content, _charset='utf8')
    # 发件人
    msg['From'] = 'm16639931390@126.com'
    # 收件人
    msg['To'] = '1067164043@qq.com'
    # 邮件主题
    msg['Subject'] = Header('测试报告', 'utf8')
    # 第四步发送邮件
    s.sendmail(from_addr='m16639931390@126.com', to_addrs='1067164043@qq.com', msg=msg.as_string())


def send_email_file(filepath):
    # 第一步连接smtp服务
    s = smtplib.SMTP()
    # 注意163端口25，qq邮箱端口是465
    s.connect(host='smtp.126.com', port=25)
    # 第二步登录到stmp服务器
    user = 'm16639931390@126.com'
    pwd = 'BVYDHHUQPEJLDLBF'
    s.login(user=user, password=pwd)
    # 第三步发送邮件
    # 构造邮件正文
    content = '这个是用来测试的邮件，看看能不能发成功！'
    text_content = MIMEText(content, _charset='utf8')
    # 构造附件
    part = MIMEApplication(open(filepath, 'rb').read(), _subtype=None)
    part.add_header('content-disposition', 'attachment', filename='report.html')
    # 封装一封邮件
    msg = MIMEMultipart()
    # 加入附件和文本内容
    msg.attach(text_content)
    msg.attach(part)
    # 发件人
    msg['From'] = 'm16639931390@126.com'
    # 收件人
    msg['To'] = '1067164043@qq.com'
    # 邮件主题
    msg['Subject'] = Header('测试报告', 'utf8')
    # 第四步发送邮件
    s.sendmail(from_addr='m16639931390@126.com', to_addrs='1067164043@qq.com', msg=msg.as_string())
