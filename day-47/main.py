from bs4 import BeautifulSoup
import requests
import smtplib
import os

EMAIL = "joeydon21@gmail.com"
PASSWORD = os.environ.get("google_app_password")

BUY_PRICE = 20

url = ("https://www.amazon.com/Orgain-Organic-Protein-Superfoods-Vanilla/dp/B07PXNNFGT?pd_rd_w=mDlNG&content-id=amzn1."
       "sym.e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&pf_rd_p=e8faeee7-63c9-4cb3-96e0-e50a41f3b35b&pf_rd_r=1KH3Y63DEHSMQ41"
       "JRMQB&pd_rd_wg=Za9Oe&pd_rd_r=44aef683-1d51-4b9d-af0f-36db4d624b29&pd_rd_i=B07PXNNFGT&psc=1&ref_=pd_bap_d_grid"
       "_rp_0_1_ec_i")
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,es;q=0.8"
}

response = requests.get(url=url, headers=header)
website = response.text

soup = BeautifulSoup(markup=website, features="html.parser")
title = soup.find(name="span", id="productTitle").get_text().split()[0:5]
product = " ".join(title)
price = soup.find(name="span", class_="a-offscreen").get_text()
price_with_currency = price.split("$")[1]
price_as_float = float(price_with_currency)


if price_as_float < BUY_PRICE:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                      to_addrs=EMAIL,
                      msg=f"Subject:Amazon Low Price Alert!!!\n\nThe price for your {product} is now {price}!"
                          f" Here's the link to purchase!\n {url}".encode("utf-8")
                            )
