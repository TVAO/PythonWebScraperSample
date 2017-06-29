
# Request library example

import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
content = page.content
print(content)
print("\n")

# BeautifulSoup parsing and extraction example with commands

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')  # parse HTML
print(soup.prettify())  # print HTML in nice format
print("\n")

children = list(soup.children)
types = [type(item) for item in children]
html = children[2]
htmlChildren = list(html.children)
body = list(htmlChildren[3])
p_tag = body[1]
p_text = p_tag.get_text()
print(html)


# Extract specific tag with 'find_all'

soup = BeautifulSoup(page.content, 'html.parser')
p = soup.find_all('p')[0].get_text()
first_p = soup.find('p')

# Search for tags by class and id

page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
p_by_class = soup.find_all('p', class_='outer-text')
tags_by_class = soup.find_all(class_="outer-text")
element_by_id = soup.find_all(id="first")

# Search page via CSS selectors using 'select'
p_tags_inside_div = soup.select("div p")

# Debug
exit(0)