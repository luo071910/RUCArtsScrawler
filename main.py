#-*-coding:utf-8-*-
import urllib2
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read().decode("utf-8")
    return html

def parseJson(html):
    html_py = json.loads(html)
    #提取JSON文件中的有用数据
    activity_id = html_py["data"]["list"][0]["Id"] # 演出的ID标示
    title = html_py["data"]["list"][0]["Title"]      # 演出题目
    content = html_py["data"]["list"][0]["Contents"] # 演出内容
    return activity_id, title, content

def sendMail(title, content): 
    # 第三方 SMTP 服务
    mail_host="*********"  #设置服务器
    mail_user="*********"    #用户名
    mail_pass="*********"   #口令 

    sender = '**********'
    receivers = '***********'  # 接收邮箱
    
    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receivers

    subject = title
    message['Subject'] = Header(subject, 'utf-8')

    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host)    # 默认25为SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "邮件发送成功"

# 判断该活动是否为新活动, activity_IDs.json用来储存已抓取过的活动ID。
def isNewID(activity_id):
    with open('activity_IDs.json', 'r') as json_file:
        data = json.load(json_file)
    if activity_id in data["activity_IDs"]:
        return False
    else:
        with open('activity_IDs.json', 'w') as json_file:
            data["activity_IDs"].append(activity_id)
            json_file.write(json.dumps(data))
        return True
        
if __name__ == "__main__":
    url = "http://univ.gurucv.com/artsruc/thing/list?startId=1&type=1&cvnumber=130256&pid=0"
    html = getHtml(url)
    activity_id, title, content = parseJson(html)
    content = content + "<a href=http://univ.gurucv.com/artsruc/?pageActivitySee?id=" + str(activity_id) + ">点击我前往艺术团官网</a>".decode('utf-8')
    if (isNewID(activity_id)):
        sendMail(title, content)
    else:
        print "活动未更新"
