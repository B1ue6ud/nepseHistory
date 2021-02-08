import bs4, json

req = open('Nepse Index History - Nepal Stock Information.htm', 'r')

soup = bs4.BeautifulSoup(req, "lxml")

print(soup.title.string)

json_obj=[]

tables = soup.find_all('table')

table_rows = tables[0].find_all('tr')
for tr in table_rows:
	d_list=[]
	for td in tr:
		data = td.string
		d_list.append(data)
	json_obj.append({
                'sn' : d_list[1],
                'date' : d_list[3],
                'open' : d_list[5],
                'high' : d_list[7],
                'low' : d_list[9],
                'close' : d_list[11],
                'absolute' : d_list[13],
                'percentage' : d_list[15],
                'volume' : d_list[17],
                'trunover' : d_list[19]
                })

with open('nepse_history_data.json','w') as jsonfile:
    json.dump(json_obj, jsonfile)

'''

import json
#Create a JSON Object
json_obj = {}
json_obj['employees'] = []
json_obj['employees'].append({
    'emp_name' : 'John Watson',
    'date_of_join' : '01-01-2015'
    })
#Write the object to file.
with open('example.json','w') as jsonFile:
    json.dump(json_obj, jsonFile)'''
