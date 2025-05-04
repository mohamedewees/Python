import datetime
from urllib.request import urlopen
import requests



url_10gm = 'https://shop.btcegyptgold.com/shop/10gm-307?category=90#attr=1523,1529,1801'
url_5gm = 'https://shop.btcegyptgold.com/shop/5gm-335?category=90#attr=1681,1687,1840'
url_coin_quarter = 'https://shop.btcegyptgold.com/shop/2gm-322?category=92#attr=1583,1587,1850'

page_10gm = urlopen(url_10gm)
page_5gm = urlopen(url_5gm)
page_coins_quarter = urlopen(url_coin_quarter)


html_bytes_10gm = page_10gm.read()
html_bytes_5gm = page_5gm.read()
html_bytes_quarter = page_coins_quarter.read()

html_10gm = html_bytes_10gm.decode("utf-8")
html_5gm = html_bytes_5gm.decode("utf-8")
html_quarter = html_bytes_quarter.decode("utf-8")

cost_index_10gm = html_10gm.find('<span class="oe_currency_value">')
cost_index_5gm = html_5gm.find('<span class="oe_currency_value">')
cost_index_quarter = html_quarter.find('<span class="oe_currency_value">')

cost_index_start_10gm = cost_index_10gm + len('<span class="oe_currency_value">')
cost_10gm = html_10gm[cost_index_start_10gm:(cost_index_start_10gm+6)]

cost_index_start_5gm = cost_index_5gm + len('<span class="oe_currency_value">')
cost_5gm = html_5gm[cost_index_start_5gm:(cost_index_start_5gm+6)]

cost_index_start_quarter = cost_index_quarter + len('<span class="oe_currency_value">')
cost_quarter = html_quarter[cost_index_start_quarter:(cost_index_start_quarter + 6)]



message = (("Date/Time: " + datetime.datetime.now().strftime("%d/%m/%Y, %I:%M:%S %p") +
           "\r\n" + "\u00bb " + "BTC Ingot(10gm) price: " + cost_10gm+ " LE") +
           "\r\n" + "\u00bb " + "BTC Ingot(5gm) price: " + cost_5gm+ " LE" +
           "\r\n" + "\u00bb " + "BTC Coins(2gm) price: " + cost_quarter+ " LE")

print("Current date / time: " + datetime.datetime.now().strftime("%d/%m/%Y , %I:%M:%S %p"))
print("\u00bb " + "BTC Ingot(10gm) price: " +cost_10gm+ " LE")
print("\u00bb " + "BTC Ingot(5gm) price: " +cost_5gm+ " LE")
print("\u00bb " + "BTC Coins(2gm) price: " +cost_quarter+ " LE")

token = '7476528415:AAE9Nz8-ZVv78-CwHmeBzHLsFe6BlT3mdYE'
chat_id = "-4749799913"
url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={message}"
chats = requests.get(url)