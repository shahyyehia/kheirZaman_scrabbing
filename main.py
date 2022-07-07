import requests

import xlsxwriter

# Workbook() takes one, non-optional, argument
# which is the filename that we want to create.
workbook = xlsxwriter.Workbook('kheirzaman.xlsx')

worksheet = workbook.add_worksheet()

worksheet.write('A1', 'name..')
worksheet.write('B1', 'price')



payload={}
headers = {
  'deviceId': 'l59exvuo9wduzj1nx24',
  'Accept': 'application/json, text/plain, */*',
  'Referer': 'https://www.kheirzaman.com/en/category/1/12/Groceries',
  'Sec-Fetch-Dest': 'empty',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
  'content-language': 'en'
}



row=0
worksheet.write(row, 0, "name")
worksheet.write(row, 1, "price")
row+=1
for category_number in range(1,24):
    url = "https://www.kheirzaman.com/portals/public/api/products/filter?categoryIds[0]="+str(category_number)+"&level=1"
    response = requests.request("GET", url, headers=headers, data=payload)
    pages=response.json()['data']['pagination']['totalPages']
    for i in range(pages):
        url = "https://www.kheirzaman.com/portals/public/api/products/filter?categoryIds[0]="+str(category_number)+"&level=1&page="+str(i)
        response = requests.request("GET", url, headers=headers, data=payload)
        products=len(response.json()['data']['products'])
        for j in range(products):
            worksheet.write(row, 0, response.json()['data']['products'][j]['name'])
            worksheet.write(row, 1, response.json()['data']['products'][j]['finalPrice'])
            row += 1
            print("product: ",response.json()['data']['products'][j]['name'])
            print("price: ",response.json()['data']['products'][j]['finalPrice'])
    print("---------------------------------------------------------------------")

workbook.close()