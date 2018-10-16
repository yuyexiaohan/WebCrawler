# coding=utf-8 
# Time : 2018/10/15 11:17 
# Author : achjiang
# File : load_onepiece.py
# coding=utf-8
# Time : 2018/10/15 9:21
# Author : achjiang
# File : test1.py
import requests     # 爬虫的专用网站数据模块
from bs4 import BeautifulSoup   # 将文本划分为对象
import uuid     # 导入随机数生成模块
import re

"""爬虫示例：简单爬去一个网站的文件img,并保存到本地"""
# 1.获取url的网络源代码
response = requests.get(url='http://hanhuazu.cc/cartoon/post?id=11133')
# 2.需要根据实际的编码方式进行编码，否则会出现乱码
# response.encoding = 'gbk'
print(response)
# 3.实例化一个，将text以html文本分析器的方式进行解析
soup = BeautifulSoup(response.text, features='html.parser')
# 4.查找解析后的文本中的内容,对html文件而言，都是可以将标签
# 理解为对象，每个对象中又包含有多个对象。head/body -> div -> p ...
target = soup.find_all("div" ,class_='post-img')
print(target, type(target))
# 5.缩小范围，find查找第一个数据，find_all查找文本所有的数据
# li_list = target.find_all('p')   # 查找对象内的所有的li标签的列表

# 6.对列表中的对象进行遍历，查找具体的内容
# for i in li_list:
# 	# 找到标签后，返回具体内容
# 	img_src = i.find('img').attrs.get('src')
# 	if img_src:
# 		# 7.保存筛选出来的内容
# 		# 根据获取的图片url获取数据,其中img_response必须是一个
# 		# 完整的http://XXXXX类的格式
# 		img_response = requests.get(url=('http:' + img_src))
# 		# file_name = text + '.jpg'   # 其中获取的text遍历中存在‘/’等符号
# 		j = 0
# 		file_name = str(j) + '.' + str(re.split(r'\.', img_src)[-1])
# 		j += 1
# 		try:
# 			with open(file_name, 'wb') as f:
# 				f.write (img_response.content)
# 		except OSError as e:
# 			print('error:',e)






