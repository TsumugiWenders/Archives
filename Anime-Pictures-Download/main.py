import traceback
import urllib
from time import sleep
import requests
from bs4 import BeautifulSoup
import os

def requestsdownload(url, filename):
    if os.path.exists(filename):
        print('file exists!')
        return
    try:
        r = requests.get(url, stream=True, timeout=60)
        r.raise_for_status()
        with open(filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    f.flush()
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
        url = "http://yadar.net/post/show/"+str(i)
        html = requests.get(url).text
        soup = BeautifulSoup(html, 'html.parser')
        for img in soup.find_all('img', class_="image"):
            target_url =img['src']
            filename = os.path.join('IMG', str(i) + "."+target_url.split('.')[-1])
            print(target_url)
            print(filename)
            requestsdownload(target_url,filename)
            print("This img Download!")
            sleep(1)
            os.system('cls')
