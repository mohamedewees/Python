import requests
url = 'https://shop.bulliontradingcenter.com/product/10g-ingot-btc'  # Example API
response = requests.get(url)

print(response.text)
