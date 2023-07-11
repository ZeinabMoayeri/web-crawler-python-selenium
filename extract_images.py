import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# Set up the webdriver
driver = webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver, 10)
df = pd.read_csv('all_products_with_deatails.csv')
urls = df['Links']
if not os.path.exists('images/'):
    os.mkdir('images')


titles = 1687
for url in urls:
    
    driver.get(url)
    title = driver.title
    print(title)
    driver.implicitly_wait(5)
    wait = WebDriverWait(driver, 5)

    # Find all image elements
    image_elements = driver.find_elements(By.TAG_NAME, 'img')
    print(f"Found {len(image_elements)} images on the page.")

    # Create a directory to save the images
    if not os.path.exists(f'images/{titles}'):
        os.mkdir(f'images/{titles}')

    # Loop through the image elements and save each image
    for i, img in enumerate(image_elements):
        src = img.get_attribute('src')
        if src is not None and 'http' in src:
            response = requests.get(src)
            with open(f'images/{titles}/image_{i}.jpg', 'wb') as f:
                f.write(response.content)
                print(f"Saved image_{i}.jpg")
    
    titles += 1
