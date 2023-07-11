# import os
# import requests
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Set up the webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)

# # Navigate to the webpage
# url = "https://diza.gallery/product-2402/anardoneh_black_earrings_Asoo_Diza#570863258"
# driver.get(url)
# title = driver.title
# print(title)
# driver.implicitly_wait(0.5)
# first = driver.find_element(By.CLASS_NAME, 'ipiGalleryItem')
# # print(f"{first.text}")
# print(first.get_attribute('src'))

# # WebDriverWait(driver, 30).untill(
# #     EC.text_to_be_present_in_element
# # )




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
df = pd.read_csv('all_products_with_deatails - products_extract_with_detail (3).csv')
urls = df['Links']
# urls = [
#     'https://diza.gallery/product-1001/mini_scarf_dogsandeyes_rosebari_diza#685327', 
#     'https://diza.gallery/product-1006/dogsandeyes_orange_Top_rosebari_diza#3672123', 
#     'https://diza.gallery/product-1007/shamsolemareh_bronze_earrings_SaraRazmi_diza#5762228', 
#     'https://diza.gallery/product-1009/triplet_necklace_sararazmi_diza#368811', 
#     'https://diza.gallery/product-1010/blue_monster_headpiece_rosebari_diza#3561115', 
#     'https://diza.gallery/product-1011/talaat_silver_earrings_elhamalirezaei_diza#3673114', 
#     'https://diza.gallery/product-1012/silver_dot_bracelet_elhamalirezaei_diza#3572224', 
#     'https://diza.gallery/product-1013/silver_earrings_3crystal_elhamalirezaei_diza#357117', 
#     'https://diza.gallery/product-1014/lionandsun_headpiece_rosebari_diza#357811965', 
#     'https://diza.gallery/product-1015/several_fabrics_blouse_ramakzaringhaba_diza#47832'
# ]

if not os.path.exists('images/'):
    os.mkdir('images')


titles = 2646
for url in urls:
    
    # Navigate to the webpage
    # url = "https://diza.gallery/product-2402/anardoneh_black_earrings_Asoo_Diza#570863258"
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

