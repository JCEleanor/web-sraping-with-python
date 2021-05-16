import requests
import bs4
from get_products import get_products

def sort_products():

    success_count=0
    fail_count=0
    pId = 0
    all_products = get_products()

    for product in all_products:

        product_detail_url = "http://www.swanpanasia.com/products/{}"
        r = requests.get(product_detail_url.format(product["eng_name"]))

        if r.status_code == 200:
            print("success 200", product_detail_url.format(product["eng_name"]))
            success_count +=1
            r.encoding = "utf-8"
            soup = bs4.BeautifulSoup(r.text,'lxml')

            #product id 
            pId += 1
            product["pId"] = pId

            description = soup.select(".product_intro_rich.w-richtext>p")
            product["description"] = description[0].text

            tags = soup.select(".tag-text")
            product["tags"] = [tag.text for tag in tags]

            price = soup.select(".enh2.tan")
            product["price"] = int(price[0].text)

            notes = soup.select(".p1.tan.inline")
            product["notes"] = notes[0].text.replace("｜", " ").split(" ")                     

        elif r.status_code != 200:

            product["pId"] = 0
            print("Fail ",r.status_code, ": ", product["ch_name"], product["eng_name"])
            fail_count+=1

    print("success:  ", success_count)
    print("failed:  ", fail_count)


    all_products = [i for i in all_products if i["pId"] != 0]

    del_products = [i for i in all_products if i["pId"] == 0]
    print("remove products: ", len(del_products))
    del del_products

    print("total product count: ", len(all_products))
    return all_products