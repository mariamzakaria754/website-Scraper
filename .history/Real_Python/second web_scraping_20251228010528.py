# استخدام Beautiful Soup لتحليل صفحات HTML
#  قراءة صفحة HTML باستخدام Beautiful Soup
from bs4 import BeautifulSoup
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf-8")

# تنشئ كائن لتحليل HTML باستخدام محلل بايثون المدمج.
soup = BeautifulSoup(html, "html.parser")
# BeautifulSoupاستخدام
# لاستخلاص كل النص من الصفحة (بدون وسوم HTML):
print(soup.get_text())
# لاستخلاص كل الصور (وسوم <img>):
print(soup.find_all("img"))
# للوصول إلى خاصية مثل src لصورة
images = soup.find_all("img")
print(images[0]["src"])
# لاستخلاص عنوان الصفحة
print(soup.title.string)
# لاستخلاص وسم معين بشرط
print(soup.find_all("img", src ="/static/dionysus.jpg" ))

