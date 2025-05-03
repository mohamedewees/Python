# <span class="oe_price" style="white-space: nowrap;" data-oe-type="monetary" data-oe-expression="combination_info['price']"><span class="oe_currency_value">53,936.67</span>&nbsp;LE</span>
# <span class="oe_currency_value">26,973.34</span>
# <span class="oe_currency_value">9,456.10</span>

from urllib.request import urlopen

url_10gm = 'https://shop.btcegyptgold.com/shop/10gm-307?category=90#attr=1523,1529,1801'
url_5gm = 'https://shop.btcegyptgold.com/shop/5gm-335?category=90#attr=1681,1687,1840'
url_coin_quarter = 'https://shop.btcegyptgold.com/shop/2gm-322?category=92#attr=1583,1587,1850'

page_10gm = urlopen(url_10gm)
page_5gm = urlopen(url_5gm)
page_coins_quarter = urlopen(url_coin_quarter)

# print(page)
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

print("BTC Ingot(10gm) price: " +cost_10gm+ " LE")
print("BTC Ingot(5gm) price: " +cost_5gm+ " LE")
print("BTC Coins(2gm) price: " +cost_quarter+ " LE")
# print(cost_index_start)
