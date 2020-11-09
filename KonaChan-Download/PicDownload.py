import traceback
import urllib
from time import sleep
import requests
from bs4 import BeautifulSoup
import os

def urllibdownload(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        urllib.request.urlretrieve(url,filename)
        return filename
    except KeyboardInterrupt:
        if os.path.exists(filename):
            os.remove(filename)
        raise KeyboardInterrupt
    except Exception:
        traceback.print_exc()
        if os.path.exists(filename):
            os.remove(filename)

if __name__ == '__main__':
    if os.path.exists('IMG') is False:
        os.makedirs('IMG')
    start = 300000
    #end = 600000
    end = 300020
    for i in range(start,end+1):
        url = "http://konachan.net/post/show/"+str(i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img', class_="image"):
            target_url =img['src']
            filename = os.path.join('IMG', str(i) + "."+target_url.split('.')[-1])
            print(target_url)
            print(filename)
            #requestsdownload(target_url,filename)
            urllibdownload(target_url,filename)
            print("This img Download!")
            sleep(1)
            os.system('cls')
