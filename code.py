from bs4 import BeautifulSoup
import requests


run = True
num = 2
n = 0
while run:
    try:
        i = 0
        if num ==18:
            a = 8/0
        url = f"https://www.jumia.ma/ordinateurs-pc/?page={num}"
        responce = requests.get(url).text
        print(url,"\n")
        soup = BeautifulSoup(responce,"lxml")
        body = soup.find_all("article",class_="prd _fb col c-prd")
        for article in body:
            fa = article.h3.text
            prc = soup.find_all("div",class_ = "prc")[i]
            print("\n",fa)
            print(prc.text)
            n+=1
            i+=1
        num+=1
        continue
    except:
        run = False
print(f" \n \n {n} articles au total !!")
