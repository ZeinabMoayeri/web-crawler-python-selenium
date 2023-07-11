#### Introduction

This is a store site from which all the text information along with product photos are extracted.

1. At first, we wait until all the products are loaded on the page.
   Then we save that page in HTML format.
2. Then we run the Jupiter file to extract all page information + links of all products.
3. Then we go to the link of each product and extract the information of each product in addition to all its photos and save each one in a folder.

#### Installation

First, we install the required libraries with the following command:

` pip install requests` 

`pip install selenium`

`pip install pandas `

The Version of these libraries, that I use, is in the requirements.txt file

##### 1. Load the main page & save that

##### 2. Extract all data of Products

 run the Jupiter file that name is "DizaGallery_Scrap.ipynb" to extract names, links, designers, and prices.

##### 3. Run extract_images.py
to extract all images for each product & save that own folder

##### 4. Run extract_details.py
to extract all details for each product & save that on a CSV file
if I want to extract all text on the product page, run "extract_ipibox.py"

