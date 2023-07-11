# import os
# import pandas as pd
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


# # df = pd.read_csv('filespart2.csv')
# # urls = df['Links']
# urls = [
#     'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#36890632', 
#     'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#457995270', 
#     'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#4790632', 
#     'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#4791109646', 
#     'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#135906342', 
#     'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#3579731479', 
#     'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#53214379', 
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

# # Set up the webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# wait = WebDriverWait(driver, 10)

# class_names = [
#     "thisbrand",  
#     "ipih1", 
#     # "sizedetails", 
#     "sizedetail", 
#     "ipiBoxi"
# ]
# brands= []
# iphih1 = []
# # sizedetails = []
# sizedetail = []
# ipiBoxi = []

# i = 0
# for url in urls:
#     driver.get(url)
#     title = driver.title

#     text_data = {}
#     for class_name in class_names:
#         elements = driver.find_elements(By.CLASS_NAME, class_name)
#         if len(elements) > 0:
#             text_data[class_name] = [element.text for element in elements]
#             # print(f"Found {len(elements)} elements with class name '{class_name}'.")
#         else:
#             text_data[class_name] = 'None'

#     # Save the text data to a file
#     if len(text_data) > 0:
#         with open('text_data.txt', 'w', encoding='utf-8') as f:
#             for class_name, texts in text_data.items():
#                 if class_name == "thisbrand" :
#                     brands.append(texts)
#                 elif class_name == "ipih1" :
#                     iphih1.append(texts)
#                 # elif class_name == "sizedetails" :
#                 #     sizedetails.append(texts)
#                 elif class_name == "sizedetail" :
#                     sizedetail.append(texts)
#                 elif class_name == "ipiBoxi" :
#                     ipiBoxi.append(texts)
#                     print(url)
#                     print(texts)

#     else:
#         print("No text data found on the page.")

#     print(f"Page {i}_{title} DONE-------------------------------.")
#     i += 1


# all_data = {
#     'url' : urls, 'brands' : brands, 'iphih1' : iphih1, 
#     'sizedetail' : sizedetail, 'ipiBoxi' : ipiBoxi
# }

# # all_data = {
# #     'url' : urls, 'brands' : brands, 'iphih1' : iphih1, 'sizedetails' : sizedetails, 
# #     'sizedetail' : sizedetail, 'ipiBoxi' : ipiBoxi
# # }


# df = pd.DataFrame(all_data)
# df.to_csv('Test.csv')



import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException



urls = [
    'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#36890632', 
    'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#3579731479', 
    'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#4790632', 
    'https://diza.gallery/product-1013/silver_earrings_3crystal_elhamalirezaei_diza#357117', 
    'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#4791109646', 
    'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#135906342', 
    'https://diza.gallery/product-2188/iran_vest_Jutti9_Diza#457995270', 
    'https://diza.gallery/product-2189/iran_trousars_Jutti9_Diza#53214379', 
    'https://diza.gallery/product-1006/dogsandeyes_orange_Top_rosebari_diza#3672123', 
    'https://diza.gallery/product-1007/shamsolemareh_bronze_earrings_SaraRazmi_diza#5762228', 
    'https://diza.gallery/product-1009/triplet_necklace_sararazmi_diza#368811', 
    'https://diza.gallery/product-1010/blue_monster_headpiece_rosebari_diza#3561115', 
    'https://diza.gallery/product-1011/talaat_silver_earrings_elhamalirezaei_diza#3673114', 
    'https://diza.gallery/product-1012/silver_dot_bracelet_elhamalirezaei_diza#3572224', 
    'https://diza.gallery/product-1014/lionandsun_headpiece_rosebari_diza#357811965', 
    'https://diza.gallery/product-1015/several_fabrics_blouse_ramakzaringhaba_diza#47832', 
    'https://diza.gallery/product-1136/ghalamkar_gkt_RezaNadimi_Diza#468095447'
]

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

# with open('1111111111111111.txt', 'a', encoding='utf-8') as file:
#     file.write(url)
#     file.write(ipiBoxi)

df = pd.DataFrame(all_data)
df.to_csv('Test.csv')

