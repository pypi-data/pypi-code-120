'''
Created by auto_sdk on 2020.11.26
'''
from seven_top.top.api.base import RestApi
class JstMiniappCrowdCreateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.crowd_name = None
		self.description = None
		self.end_date = None
		self.start_date = None

	def getapiname(self):
		return 'taobao.jst.miniapp.crowd.create'
