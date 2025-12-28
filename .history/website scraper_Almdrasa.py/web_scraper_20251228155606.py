
# Select website that we are going to scrape
# this is  a new line
import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/"
# response = تخزين نتيجة الطلب  هنا
response = requests.get(url)
if response.status_code == 200:
    # BeautifulSoup نحلل البيانات باستخدام
   soup = BeautifulSoup(response.content,  "html.parser")

    # استخراج لمعلومات الكتب
   #باستخدام المحدد
   books = soup.find_all("article")
   print(books[0])
   # استخراج عناويين الكتب والتقييمات حالة التوفر والسعر
for book in books:
    title = book.h3.a ["title"]
    rating = book.p["class"][1]
    availability = book.find("p", class_ ="instock availability" ).text.strip()
    price = book.find("p", class_ ="price_color" ).text
    print(" book titled : " + title + " has a rating of \n"
      + rating + " stars, " + "Availability status is " + availability + ", price " + price )
else:
    print(f"Failed to load the page. Status code: {response.status_code}")





