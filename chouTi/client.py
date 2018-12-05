# coding=utf-8 
# Time : 2018/10/15 14:52 
# Author : achjiang
# File : client.py
import requests


phone = ''
password = ''
post_dict = {
	"phone": phone,
	'password': password,
	'oneMonth': 1
}
response = requests.post(
	url="http://dig.chouti.com/login/",
	data=post_dict
)

print('--------', response.text, '--------')
cookie_dict = response.cookies.get_dict()
print(cookie_dict)

response = requests.get(
	url='https://dig.chouti.com/profile',
	cookies={
		'gpsd':'88472c6a2dbaebcfbb0fa1357f2bb573'
	}
)
