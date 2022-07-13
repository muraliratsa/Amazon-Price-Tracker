import requests
from bs4 import BeautifulSoup
from smtplib import SMTP

MY_EMAIL = "muralipythonista@gmail.com"
MY_PASSWORD = "muralipythonista23"

PRODUCT_URL = "https://www.amazon.in/Converse-Unisexs-Optical-White-Sneakers/dp/B012TRQRRQ/ref=sr_1_27?crid=1UK264F1ZPPZG&dchild=1&keywords=chuck%2Btaylors%2Ball%2Bstar%2Bconverse&qid=1621069598&sprefix=chuck%2Btaylors%2B%2Caps%2C363&sr=8-27&th=1&psc=1"

RESONABLE_PRICE = 1400

headers = {
    "Accept-Language":"en-US,en;q=0.9",
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

response = requests.get(url=PRODUCT_URL, headers=headers)
response.raise_for_status()

website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

product_title = soup.find(name="span", id="productTitle").getText().strip()

product_price_tag = soup.find(name="span", id="priceblock_ourprice")
product_live_price = int(product_price_tag.getText().split()[1].strip().replace(",", "").split(".")[0])

if product_live_price <= RESONABLE_PRICE:
    with SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="murali832001@gmail.com",
            msg=f"Subject:Price Drop!\n\n{product_title} is now available at ₹{product_live_price}.\n{PRODUCT_URL}".encode('utf-8')
        )

