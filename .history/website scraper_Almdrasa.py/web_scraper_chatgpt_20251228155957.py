import requests
from bs4 import BeautifulSoup
# this a new change 2
# الرابط الأساسي للموقع
BASE_URL = "https://books.toscrape.com/"

def fetch_page(url):
    """إرسال طلب إلى الموقع وإرجاع كائن BeautifulSoup إذا نجح الطلب."""
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, "html.parser")
    else:
        print(f"Failed to load the page. Status code: {response.status_code}")
        return None

def extract_book_info(book):
    """استخراج معلومات كتاب واحد من عنصر HTML."""
    title = book.h3.a["title"]
    rating = book.p["class"][1]
    availability = book.find("p", class_="instock availability").text.strip()
    price = book.find("p", class_="price_color").text
    return {
        "title": title,
        "rating": rating,
        "availability": availability,
        "price": price
    }

def scrape_books_from_page(soup):
    """استخراج جميع الكتب من صفحة واحدة."""
    books = soup.find_all("article", class_="product_pod")
    book_data = []
    for book in books:
        info = extract_book_info(book)
        book_data.append(info)
    return book_data

def display_books(book_list):
    """عرض قائمة الكتب التي تم استخراجها."""
    for book in book_list:
        print(f"📚 Title: {book['title']}")
        print(f"⭐ Rating: {book['rating']} stars")
        print(f"📦 Availability: {book['availability']}")
        print(f"💰 Price: {book['price']}")
        print("-" * 50)

def main():
    """الدالة الرئيسية لتشغيل البرنامج."""
    soup = fetch_page(BASE_URL)
    if soup:
        books = scrape_books_from_page(soup)
        display_books(books)

# تشغيل البرنامج إذا تم تنفيذ الملف مباشرة
if __name__ == "__main__":
    main()
