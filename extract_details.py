import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


df = pd.read_csv('all_products_with_deatails.csv')
urls = df['Links']

# Set up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

class_names = [
    "thisbrand",  
    "ipih1", 
    "sizedetails", 
    "sizedetail", 
    "ipiBoxi"
]
brands= []
iphih1 = []
sizedetails = []
sizedetail = []
ipiBoxi = []

i = 0
for url in urls:
    driver.get(url)
    title = driver.title

    text_data = {}
    for class_name in class_names:
        elements = driver.find_elements(By.CLASS_NAME, class_name)
        if len(elements) > 0:
            text_data[class_name] = [element.text for element in elements]
            # print(f"Found {len(elements)} elements with class name '{class_name}'.")
        else:
            text_data[class_name] = 'None'

    # Save the text data to a file
    if len(text_data) > 0:
        with open('text_data.txt', 'w', encoding='utf-8') as f:
            for class_name, texts in text_data.items():
                if class_name == "thisbrand" :
                    brands.append(texts)
                elif class_name == "ipih1" :
                    iphih1.append(texts)
                elif class_name == "sizedetails" :
                    sizedetails.append(texts)
                elif class_name == "sizedetail" :
                    sizedetail.append(texts)
                elif class_name == "ipiBoxi" :
                    my_list = []
                    for itemm in texts:
                        my_list.append(str(itemm))
                    ipiBoxi.append(my_list)
                    # ipiBoxi.append(texts)

    else:
        print("No text data found on the page.")

    print(f"Page {i}_{title} DONE-------------------------------.")
    i += 1


all_data = {
    'url' : urls, 'brands' : brands, 'iphih1' : iphih1, 'sizedetails' : sizedetails, 
    'sizedetail' : sizedetail, 'ipiBoxi' : ipiBoxi
}


df = pd.DataFrame(all_data)
df.to_csv('files2test.csv')

