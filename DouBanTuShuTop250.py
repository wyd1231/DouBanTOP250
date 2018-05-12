import requests
import time
from lxml import etree
w=0
for a in range(0, 250, 25):
    url = 'https://book.douban.com/top250?start={}'.format(a)
    data = requests.get(url).text

    s=etree.HTML(data)
    file=s.xpath('//*[@id="content"]/div/div[1]/div/table/tr')

    for haha in file:
        title = haha.xpath("./td[2]/div[1]/a/@title")[0]
        href = haha.xpath("./td[2]/div[1]/a/@href")[0]
        writer = haha.xpath("./td[2]/p[1]/text()")[0]
        score = haha.xpath("./td[2]/div[2]/span[2]/text()")[0]
        man = haha.xpath("./td[2]/div[2]/span[3]/text()")[0].strip("(").strip( ).strip(")")
        juzi = haha.xpath("./td[2]/p[2]/span/text()")[0]
        w=w + 1
        print("{} - {} , {} , {} , {} , {} , {}".format(w,title,juzi,href,writer,score,man))
