import requests as rq

from bs4 import BeautifulSoup

from bs4 import NavigableString

qurl='https://www.google.com/search?q=ind+vs+sl&oq=ins+vs+s&gs_lcrp=EgZjaHJvbWUqDwgBEAAYChiDARixAxiABDIGCAAQRRg5Mg8IARAAGAoYgwEYsQMYgAQyDwgCEAAYChiDARixAxiABDIPCAMQABgKGIMBGLEDGIAEMgwIBBAAGAoYsQMYgAQyEggFEAAYChiDARixAxiABBiKBTIICAYQABgDGAoyCQgHEAAYChiABDISCAgQABgKGIMBGLEDGIAEGIoFMg8ICRAAGAoYgwEYsQMYgATSAQg2Mzg4ajBqNKgCALACAQ&sourceid=chrome&ie=UTF-8#sie=m;/g/11w298688r;5;/m/021q23;dt;fp;1;;;'

qheader={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
}

resp= rq.get(url= qurl,headers= qheader)

bsoup = BeautifulSoup(resp.content,'html.parser')

print(resp.status_code)



#



data= bsoup.find_all('tr')
#print(data)

print(data[0].find('tr').find('div class'))



