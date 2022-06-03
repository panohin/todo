import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_info_from_kontur(tender_number: int) -> dict:
	link = 'https://zakupki.kontur.ru/' + str(tender_number)
	response = requests.get(link)
	print('Контур')
	if response.status_code == 200:
	    response = response.text
	    root = BeautifulSoup(response, 'html.parser')
	    tender_price = root.find("span", class_="tenderPrice").text
	    currency = tender_price.split('  ')[-1].strip()
	    price = float(tender_price.split('  ')[0].replace(' ','').replace(',', '.'))
	    date = root.find("span", class_="tender_date").text
	    time = root.find("span", class_="text__time").text
	    submission_end_date = datetime.strptime(date + time, '%d.%m.%Y%I:%M')

	    zakupki_gov_link = root.find(id='headerSourceLink')['href']

	    tender_data = {'max_price':price, 'currency':currency, 'submission_end_date': submission_end_date, 'tender_proccess_date': None,'zakupki_gov_link':zakupki_gov_link}
	    return tender_data
	else:
	    print(response.status_code)

def get_info_from_zakupkigov(link: str) -> dict:
	response = requests.get(link)
	print('ЕИС xml')
	if response.status_code == 200:
		response = response.content
		soap = BeautifulSoup(response, 'xml')
		title_soap = soap.find('purchaseObjectInfo').text
		print(title_soap)
	else:
		print(response.status_code)

def get_tender_info(tender_number: int) -> dict:
	"""
	Returns max_price, currency, datetime of end of application submission
	and date of tender process.
	"""
	kontur_tender_data = get_info_from_kontur(tender_number)
	if None in kontur_tender_data.values():
		zakupkigov_tender_data = get_info_from_zakupkigov(kontur_tender_data['zakupki_gov_link'])
	return tender_data