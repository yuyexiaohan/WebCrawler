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
response = requests.get(url='https://www.autohome.com.cn/news/')
# 2.需要根据实际的编码方式进行编码，否则会出现乱码
response.encoding = 'gbk'
# 3.实例化一个，将text以html文本分析器的方式进行解析
soup = BeautifulSoup(response.text, features='html.parser')
# 4.查找解析后的文本中的内容,对html文件而言，都是可以将标签
# 理解为对象，每个对象中又包含有多个对象。head/body -> div -> p ...
target = soup.find(id='auto-channel-lazyload-article')
# 5.缩小范围，find查找第一个数据，find_all查找文本所有的数据
li_list = target.find_all('li')   # 查找对象内的所有的li标签的列表
# obj = target.find_all('data-artidanchor')   # 查找内容，非标签查找为空

# print(response.text)    # 将获取的数据按照text方式打印
# print(target)   # 打印标签，获取这个name的标签中的内容
# print(li_list)   # 获取指定信息中更为具体的内容

# 6.对列表中的对象进行遍历，查找具体的内容
for i in li_list:
	a = i.find('a')     # 找到标签后，返回具体内容
	if a:
		# 可能存在部分li标签中不存在a标签，所以这里要作判断
		# text = a.find('h3')     # 可以直接找孙标签，返回的是对象，打印显示是class
		text = a.find('h3').text    # 如果要拿到文本则,加入text,打印显示是str
		img_src = a.find('img').attrs.get('src')
		# print(a.attrs.get('href'))  # 拿到a标签的href内容
		# print(text, type(text))     # 拿到h3标签内容
		# print(img_src, '\n','--------')  # 找img_src内容
		"""
		打印结果：
		 --------
		//www.autohome.com.cn/news/201810/923522.html#pvareaid=102624
		聘请四大投行 大众商用车IPO更进一步 <class 'str'>
		//www2.autoimg.cn/newsdfs/g28/M00/88/86/120x90_0_autohomecar__ChcCR1u-rCWAZ3zpAAGXv-E4NJI310.jpg 
		 --------
		"""
		# 7.保存筛选出来的内容
		# 根据获取的图片url获取数据,其中img_response必须是一个
		# 完整的http://XXXXX类的格式
		img_response = requests.get(url=('http:' + img_src))
		# file_name = text + '.jpg'   # 其中获取的text遍历中存在‘/’等符号
		file_name = text + '.' + str(re.split(r'\.', img_src)[-1])
		# print(file_name)    # 打印结果：走向电气化 雪铁龙全新C1或为电动车型.jpg
		# file_name = str(uuid.uuid4()) + '.jpg'   # 其中获取的text遍历中存在‘/’等符号
		# 打开一个文件命名为file_name
		try:
			with open(file_name, 'wb') as f:
				f.write (img_response.content)
		except OSError as e:
			print('error:',e)






