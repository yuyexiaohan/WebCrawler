# coding=utf-8 
# Time : 2018/10/15 15:13 
# Author : achjiang
# File : test1.py
import requests
import json


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                             ' Chrome/62.0.3202.75 Safari/537.36'}

response = requests.post(
	url='https://dig.chouti.com/link/vote?linksId',
	cookies={
		'gpsd':'88472c6a2dbaebcfbb0fa1357f2bb573'
	}
)

print(response.text)