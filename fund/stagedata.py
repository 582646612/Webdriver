import re
import requests
from dbinsert import DBHelper
def get_data(x):
    orc_url ='http://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jdzf&code='+str(x)
    res = requests.get(orc_url).text
    # soup = BeautifulSoup(res.text, "html.parser")
    # items = soup.find_all('li',class_='title')
    pattern = re.compile("<li class='title'>.*?</li><li class='.*?'>.*?</li><li class='.*?'>.*?</li><li class='.*?'>(.*?)</li>", re.S)
    items = re.findall(pattern, res)
    return items
if __name__ == '__main__':
    x = ['310318', '000011', '050011', '310318', '530015', '539001', '163407', '005156', '180008', '000809']
    y = ['股票型', '混合型', '债券型', '指数型', 'ETF', 'QDII', 'LOF', 'FOF', '货币型', '理财型']
    db = DBHelper()
    for i in range(0, 10):
        try:
            # print(x[i])
            items = get_data(x[i])
            print(items[0])
            # db.insertstagefund(y[i],items)
        except Exception as e:
            print(e)

