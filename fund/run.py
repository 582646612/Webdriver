from scrapy import cmdline
cmdline.execute('scrapy crawl funding'.split())
#
# import urllib.request
# from bs4 import BeautifulSoup
# url='http://fund.eastmoney.com/000001.html'
# headers1 = {'User-Agent': 'ua.random'}
#
# response = urllib.request.urlopen(url)
# content = response.read().decode('utf-8')
# #
# soup = BeautifulSoup(content, 'html.parser')
# tags= soup.find_all('dd')
# a=soup.find('span',class_='fix_fcode').get_text()
# items = soup.find_all(class_='infoOfFund')[0].select('td')
# b = soup.find('span', class_='fix_fname').get_text()
# m1=(tags[1].find_all('span')[1].string)
# y1=(tags[2].find_all('span')[1].string)
# m3=(tags[4].find_all('span')[1].string)
# y3=(tags[5].find_all('span')[1].string)
# m6=(tags[7].find_all('span')[1].string)
# rece=(tags[8].find_all('span')[1].string)
#
# print(tags[3].find_all('span')[0].string)
# print(tags[3].find_all('span')[1].string)
# print(tags[6].find_all('span')[0].string)
#
# print(items[0].get_text())
# print(items[1].get_text())
# print(items[2].get_text())
# print(items[3].get_text())
# print(items[4].get_text())
# print(items[5].get_text())