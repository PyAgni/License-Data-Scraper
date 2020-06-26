#python imports
from bs4 import BeautifulSoup
import json
import re
import requests
from pprint import pprint

#project level imports
from .getTableData import get_table_data

get_url = 'https://parivahan.gov.in/rcdlstatus/?pur_cd=101'
post_url = 'https://parivahan.gov.in/rcdlstatus/vahan/rcDlHome.xhtml'


class getDetails:
	"""
	This class scrapes driving liscense data from parivahan.gov.in
	"""
	def __init__(self,dl_no,dob):

		self.dl_no = dl_no
		self.dob = dob

	def get_session(self, soup):

		viewstate = soup.select('input[name="javax.faces.ViewState"]')[0]['value']
		return viewstate

	def post_data(self, data, cookies):

		response = requests.post(url=post_url, data = data, cookies=cookies)
		response_data = BeautifulSoup(response.text, features='lxml')

		return response_data

	
	def scrape(self):

		data = {
		'javax.faces.partial.ajax':'true',
		'javax.faces.source':'form_rcdl:j_idt43',
		'javax.faces.partial.execute':'@all',
		'javax.faces.partial.render': 'form_rcdl:pnl_show form_rcdl:pg_show form_rcdl:rcdl_pnl',
		'form_rcdl:j_idt43':'form_rcdl:j_idt43',
		'form_rcdl':'form_rcdl',
		"form_rcdl:tf_dlNO": self.dl_no,
		'form_rcdl:tf_dob_input': self.dob,
		}

		response = requests.get(url=get_url)
		cookies=response.cookies
		soup = BeautifulSoup(response.text, 'html.parser')
		
		#get the unique viewstate
		view_state = self.get_session(soup)
		data['javax.faces.ViewState'] = view_state

		response_data = self.post_data(data, cookies)

		table_list = response_data.find_all('table')

		json_data = get_table_data(table_list).get_json()

		return json_data