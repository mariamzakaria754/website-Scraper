
# import re
# from urllib.request import urlopen
#  الدالةurlopen()لفتح رابط (URL) داخل برنامج بايثون.
# url =  "http://olympus.realpython.org/profiles/aphrodite"

# urlopen()تُعيد كائنًا من نوع 
#  لقراءة محتوى الصفحة HTTPResponse

# page = urlopen(url)
# html_bytes = page.read()            # المحتوى بصيغة bytes
# html_text = html_bytes.decode("utf-8")   # تحويله إلى نص
# print(html_text)                          # طباعة كود HTML
                      
# # استخراج المعلومات من كود html 

# pattern = "<title.*?>.*?</title.*?>"  # نمط شامل لعلامة العنوان
# match_results = re.search(pattern, html, re.IGNORECASE) # تبحث في النص عن أول html تطابق مع النمط واجعل البحث غير حساس لحالة الأحرف
# title = match_results.group()
# title = re.sub("<.*?>", "", title)  # إزالة وسوم HTML

# print(title)  


####find باستخدام 
# title_index = html.find("<title>")
# start_index = title_index + len("<title>") # بداية النص
# # 14+7 = 21
# end_index = html.find("</title>")
# title = html[start_index : end_index] # slicing التقطيع لاستخراج النص
#</title><title> نحصل على العنوان الموجود بين


# ___________________________________________________________________________________________

# استخراج النص بعد "Name:" و "Favorite Color:" باستخدام .find()
from urllib.request import urlopen
url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html_bytes = page.read()            # المحتوى بصيغة bytes
html_text = html_bytes.decode("utf-8")   # تحويله إلى نص
print(html_text)                          # طباعة كود HTML

for string in ["Name: ", "Favorite Color:"]:
    string_start_idx = html_text.find(string)
    text_start_idx = string_start_idx + len(string)

    next_html_tag_offset = html_text[text_start_idx:].find("<")
    text_end_idx = text_start_idx + next_html_tag_offset

    raw_text = html_text[text_start_idx : text_end_idx]
    clean_text = raw_text.strip(" \r\n\t")
    print(clean_text)