from selenium import webdriver
import time
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

#assert "Uzaktan Eğitim Uygulama" in driver.title


cevirKelime=input("Cevirilecek kelimeyi girin : ")

driver = webdriver.Chrome()
url = "https://www.google.com/search?q=%C3%A7eviri&oq=%C3%A7eviri&aqs=chrome.0.69i59j0i131i433i512l2j0i433i512l3j0i131i433i512j0i433i512l2j0i10i512.696j0j7&sourceid=chrome&ie=UTF-8"
driver.get(url)
elem = driver.find_element_by_xpath("//*[@id='tw-source-text-ta']")
elem.clear()
elem.send_keys(cevirKelime)
elem.send_keys(Keys.ENTER)
time.sleep(2)
sonuc=driver.find_element_by_xpath("//*[@id='tw-target-text']/span").text
print(sonuc)
#print(driver.title)
# assert "No results found." not in driver.page_source

time.sleep(5)
