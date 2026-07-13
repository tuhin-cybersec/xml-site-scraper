import requests
from bs4 import BeautifulSoup as bs
import time
import random
import csv
import os
import sys

url = 'https://www.egoscue.com/WebMenus/ePeteInstructions/{}.xml'

# আপনার মোবাইল ক্রোম ব্রাউজার হুবহু যা যা হেডার পাঠায়, তার একটি কমপ্লিট ডিকশনারি
headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'sec-ch-ua': '"Chromium";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'Connection': 'keep-alive'
}

file_name = 'sample_data.csv'
file_exists = os.path.exists(file_name)

if not file_exists:
	with open(file_name, 'a' ,newline='',encoding='utf-8') as file:
		writer = csv.writer(file)
		writer.writerow(['Name','Description'])


for i in range(10,311):
	final_url = url.format(i)
	print(f"downloading page:{final_url}")
	try:
		res = requests.get(final_url,headers=headers,allow_redirects=False,timeout=(10,10))
		res.raise_for_status()
		if res.url != f'https://www.egoscue.com/WebMenus/ePeteInstructions/{i}.xml':
			print('url ta redirect hoyeche')
			continue
		soup = bs(res.content,'xml')
		name_element = soup.select('exercise')

		if not name_element:
			print(f"page number {i}: data not found")
			continue
		name = name_element[0].get('name')

		inst_element = soup.select('instruction')

		if not inst_element:
			print(f"Instruction data not found,page-{i}")
			continue

		li_inst = []
		for element in inst_element:
			inst_text = element.get('text')
			li_inst.append(inst_text)

		all_instruction = '\n'.join(li_inst)

		purpose_element = soup.select('purpose')

		if not purpose_element:
			print(f"Purpose data not found,page-{i}")
			continue

		li_purpose = []
		for pur_ele in purpose_element:
			purpose_text = pur_ele.get('text')
			li_purpose.append(purpose_text)

		all_purpose = '\n'.join(li_purpose)
		des = f"How to Perform this E-cise™\n\n{all_instruction}\n\nFun Facts\n\n{all_purpose}"

		with open(file_name,'a',newline='',encoding='utf-8') as file:
			writer = csv.writer(file)
			writer.writerow([name,des])

		sleep_time = random.uniform(1.5,3.5)
		time.sleep(sleep_time)

	except requests.exceptions.ConnectionError as er:
		print("network disconnected...")
		sys.exit()

	except Exception as ex:
		print(f"There is a problem:{ex}")


