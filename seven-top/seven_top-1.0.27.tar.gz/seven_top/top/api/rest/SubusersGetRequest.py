'''
Created by auto_sdk on 2018.07.25
'''
from seven_top.top.api.base import RestApi
class SubusersGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.user_nick = None

	def getapiname(self):
		return 'taobao.subusers.get'
