from urllib.request import urlopen as Ureq
from bs4 import BeautifulSoup as soup

my_url = "https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48"

# opening up connection, grabbing the page
uClient = Ureq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("div",{"class": "item-container"})

filename = "products.csv"
f = open(filename, "w")

headers = "brand, product_name, shipping\n"

f.write(headers)

for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class": "item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li", {"class": "price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand:" + brand)
    print("product name:" + product_name)
    print("shipping:" + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")

f.close()