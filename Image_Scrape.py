# Program to scrape images from a given URL in a very lucid language

from bs4 import BeautifulSoup as BS
import requests
import urllib.request


first_half = 'https://www.google.com/search?q='
left_over = '+images&sxsrf=APq-WBv8a41PjPq3A3_LPfW2oYYjybAW0A:1647082397085&source=lnms&tbm=isch&sa=X&ved=2ahUKEwi5nsaJtMD2AhUSFogKHc-NAp8Q_AUoAXoECAEQAw&biw=811&bih=625&dpr=1'

Obj = input('Enter Object name ')               # enter the name of objects whose image you want to scrape
URL = first_half + Obj + left_over
r = requests.get(URL)
Data = BS(r.text,'html.parser')
ImgList = Data.findAll('img')
#print(ImgList)

for i in range(1,11):           # Put the number of Images you want to scrape
        link=ImgList[i].get('src')
        print(i,link)
        urllib.request.urlretrieve(link,'G:/'+Obj+'_'+str(i)+'.jpg')
