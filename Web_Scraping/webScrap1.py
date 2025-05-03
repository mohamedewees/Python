from urllib.request import urlopen

url = 'http://olympus.realpython.org/profiles/aphrodite'
page = urlopen(url)

print(page)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
title_index = html.find("<title>")
start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]
print(html)
print(title_index)
print(start_index)
print(title)