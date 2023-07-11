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
    "ipiBoxi",
    # "ipiBoxi_tag"
]

ipiBoxi = []
# ipiBoxi_tag = []

i = 0
for url in urls:
    driver.get(url)
    title = driver.title

    text_data = {}
    for class_name in class_names:
        # elements = driver.find_elements(By.CLASS_NAME, class_name)
        wait.until(lambda driver: driver.find_elements(By.CLASS_NAME, class_name))
        elements = driver.find_elements(By.CLASS_NAME, class_name)

        if len(elements) > 0:
            text_data[class_name] = [element.text for element in elements]
            # print(f"Found {len(elements)} elements with class name '{class_name}'.")
        else:
            text_data[class_name] = 'None'

    # Save the text data to a file
    if len(text_data) > 0:
        with open('data.txt', 'a', encoding='utf-8') as f:
            for class_name, texts in text_data.items():
                if class_name == "ipiBoxi" :
                    f.write(str(i))
                    f.write('\n')
                    f.write( url)
                    # f.write('\n')
                    # f.write(str(class_name))
                    # f.write('\n')

                    if type(texts) == list:
                        my_list = []
                        for itemm in texts:
                            my_list.append(str(itemm))

                            # f.write('|NEXT|')
                            f.write('\n')
                            f.write(str(itemm))
                            # f.write('\n')
                        ipiBoxi.append(my_list)

                    else: 
                        f.write('\n')
                        f.write('None')

                    f.write('\n')
    i += 1




all_data = {
    'url' : urls, 'ipiBoxi' : ipiBoxi
}

df = pd.DataFrame(all_data)
df.to_csv('Test.csv')

