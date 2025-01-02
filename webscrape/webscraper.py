import requests

url = "https://timesofindia.indiatimes.com/city/delhi"

def fetchandsavetofile(url,path):
    r = requests.get(url)
    with open(path,"w",encoding="utf-8") as f:
        f.write(r.text)


fetchandsavetofile(url,"times.html")
# res = requests.get(url)
# data = res.json()
# print(data)