'''
Created by auto_sdk on 2020.07.21
'''
from seven_top.top.api.base import RestApi
class ItemsCustomGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.outer_id = None

	def getapiname(self):
		return 'taobao.items.custom.get'
