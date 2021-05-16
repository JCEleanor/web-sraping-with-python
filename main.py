import csv
from sort_products import sort_products
from get_str import get_str

final_result = sort_products()

file_to_output = open('to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['pId','ch_name','eng_name', 'description', 'tags', 'price','notes', 'img_src'])

for i in final_result:
    pId = i['pId']
    ch_name = i['ch_name']
    eng_name = i['eng_name']
    dec = i['description']
    tags = [j for j in i['tags']]
    price = i['price']
    notes = i['notes']
    img_src = i['img_src']
    
    csv_writer.writerows([[pId, ch_name, eng_name, dec, get_str(tags), price, get_str(notes), img_src]])
    
file_to_output.close()  
    