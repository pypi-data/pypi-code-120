'''
Created by auto_sdk on 2020.10.26
'''
from seven_top.top.api.base import RestApi
class TraderatesGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.end_date = None
		self.fields = None
		self.num_iid = None
		self.page_no = None
		self.page_size = None
		self.peer_nick = None
		self.rate_type = None
		self.result = None
		self.role = None
		self.start_date = None
		self.tid = None
		self.use_has_next = None

	def getapiname(self):
		return 'taobao.traderates.get'
