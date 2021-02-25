import requests
import re
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74'
    }
pin = []
pl = []
page = '1614221515365'
cursor = '0'

for i in range(0, 1000):
    url = 'https://coral.qq.com/article/5963120294/comment/v2?callback=_article5963120294commentv2&orinum=10&oriorder=o&pageflag=1&cursor=' + cursor + '&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=1&_=' + str(page)
    html = requests.get(url, headers=headers).content.decode()

    pin = re.compile('"content":"(.*?)"',re.S).findall(html)
    pl.append(pin)
    lastId = re.compile('"last":"(.*?)"',re.S).findall(html)[0]
    page = str(int(page) + 1)

with open('zyq.txt', 'w', encoding='utf-8') as f:
    for l in pl:
        for comment in l:
            f.write(comment)
            f.write("\n")