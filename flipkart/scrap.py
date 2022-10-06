from time import sleep
from openpyxl import Workbook
from selenium import webdriver
from webdrivermanager import ChromeDriverManager


try:
    driver = webdriver.Chrome("/chromedriver")
    driver.get("https://www.flipkart.com/")
    driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click() #login modal close btn
    driver.find_element_by_xpath("//input[@class='_3704LK']").send_keys("Dell Laptop") #search bar
    driver.find_element_by_xpath("//button[@class='L0Z3Pu']").click() #search btn
    sleep(3)
    products = driver.find_elements_by_xpath("//div[@class='_4rR01T']") #search result title
    print(products)
    prdct_name_list = []
    prdct_price_list = []

    for product in products:
        print(product)
        prdct_name_list.append(product.text)

    products_price = driver.find_elements_by_xpath("//div[@class='_30jeq3 _1_WHN1']") #price from search result

    print(products_price)
    for product_price in products_price:
        prdct_price_list.append(product_price.text)

    final_list = list(zip(prdct_name_list, prdct_price_list))
    driver.quit()
    wb = Workbook()
    wb['Sheet'].title = "Dell Laptops"
    sheet1 = wb.active

    for data in list(final_list):
        sheet1.append(data)

    wb.save("dell.xlsx")

    file = open('dell.xlsx', 'r')
    file_data = file.read()
    file_name = file.name

    print(file_name)
    print(file_data)

except Exception as e:
    print(e)