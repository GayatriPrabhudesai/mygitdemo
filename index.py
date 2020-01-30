import requests
from bs4 import BeautifulSoup
requestsflip = requests.get("https://www.flipkart.com/elica-60-cm-1100-m3-hr-auto-clean-wall-mounted-chimney/p/itmb4020ec849aad?pid=CHYFJ43XYGMHZZGH&lid=LSTCHYFJ43XYGMHZZGHZVQA9Z&marketplace=FLIPKART&srno=b_1_9&otracker=clp_metro_expandable_1_12.metroExpandable.METRO_EXPANDABLE_Elica_chimneys-store_R86O514NX1NO_wp8&fm=neo%2Fmerchandising&iid=fa2bdbdb-15db-4cbf-acac-beb2f382b1a1.CHYFJ43XYGMHZZGH.SEARCH&ppt=browse&ppn=browse&ssid=8kc5aqwywg0000001580288865493")
requestsama = requests.get("https://www.amazon.in/Elica-Filterless-Chimney-EFL-S607-VMS/dp/B07QDDDMHX/ref=sr_1_fkmr0_2?keywords=elica+60cm+1100+m3%2Fhr+auto+clean+wall+mounted+chimney&qid=1580289209&sr=8-2-fkmr0",
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'})
beautifulsoup = BeautifulSoup(requestsflip.text, 'html.parser')
tree = BeautifulSoup(requestsama.text, 'html.parser')
resultflip = beautifulsoup.find("div", {"class": "_1vC4OE _3qQ9m1"})
resultama = tree.find("span", {"class": "a-size-medium a-color-price priceBlockBuyingPriceString"})

a = resultflip.text[1:].replace(',','')
b = resultama.text[1:].replace(',','')
print(int(a))
print(float(b))
print(int(a) - float(b))

