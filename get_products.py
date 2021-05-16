import requests
import bs4
import time

def get_products():
    
    page_count = 20
    products =[]
    base_url = "http://www.swanpanasia.com/catalog/all-product?05e7af8c_page={}"

    for i in range(1, page_count+1):
        res = requests.get(base_url.format(i))
        res.encoding = "utf-8"
        #http://www.swanpanasia.com/catalog/all-product?05e7af8c_page=20

        soup = bs4.BeautifulSoup(res.text,'lxml')

        eng_names = soup.select('.cat_nameen')
        ch_names = soup.select('.cat_name_ch')    
        img_links = soup.select('.product_imgs')

        print("On page", i, "found", len(eng_names), "products and ", len(img_links), "imgs") 

        for j in range(len(img_links)):

            eng_name = eng_names[j].text.lower().replace(" ", "-")
            ch_name = ch_names[j].text
            img = img_links[j]['src']

            #add name and img to a temporary dictionary
            dic = {}
            dic["eng_name"] = eng_name
            dic["ch_name"] = ch_name
            dic["img_src"] = img
            products.append(dic)

        #time.sleep(0.5)
    return products