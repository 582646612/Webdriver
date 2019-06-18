from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time
t = time.time()
z=str(round(t * 1000))

headers = {
"Accept":"*/*",
"Content-Type":"multipart/form-data",
"Referer":"http://10.123.0.126:18210/CIS-CHAR/business/com.ailk.uchannel.commmgr.web.TfChlPreSettleAction?action=searchNewPageInit",
"Accept-Language":"zh-Hans-CN,zh-Hans;q=0.5",
"Accept-Encoding":"gzip, deflate",
"User-Agent":"Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; InfoPath.3)",
"Host":"10.123.0.126:18210",
"Content-Length":"0",
"Connection":"Keep-Alive",
"Pragma":"no-cache",
"Cookie":"JSESSIONID=14de3a575c14d3a020378f2152e6"
}
url="http://10.123.0.126:18210/CIS-CHAR/gridturnpage?action=refresh&pk=-1&condition=USERID%3D19957934%26SEARCHFLG%3D2%26CHNL_ID%3D%26CHNL_NAME%3D%26CHNL_KIND_ID%3D%26ACCOUNT_DATE%3D201905%26PURVIEW%3D1%26COMM_SRC%3DALL%26CenterValue%3D86%26CenterType%3Dcommmgr&tmpPercentWidth=1356&url_source=XMLHTTP"
d=requests.post(url,headers=headers)
print(d.text)



