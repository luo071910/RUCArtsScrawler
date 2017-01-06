# RUCArtsScrawler
##简介
自动抓取RUCArts上的赠票信息。
##使用说明
需要Python2.7来运行该程序，需要配置发送信箱与接收信箱。建议配合Cron来定时运行该程序。目前仅抓取网页上最新的一条活动并发送到接收邮箱。
##链接的格式说明

1. 该网站通过调用一个链接来获取储存活动数据的JSON数据，该链接为http://univ.gurucv.com/artsruc/thing/list?startId=1&type=1&cvnumber=130256&pid=0， 链接中的参数似乎都可以随意设置。
2. 每个活动的链接格式为http://univ.gurucv.com/artsruc/?pageActivitySee?id=XXXXXXXXXXX 。
