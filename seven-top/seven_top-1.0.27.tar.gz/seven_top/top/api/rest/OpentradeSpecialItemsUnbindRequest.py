'''
Created by auto_sdk on 2020.08.12
'''
from seven_top.top.api.base import RestApi
class OpentradeSpecialItemsUnbindRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.item_ids = None
		self.miniapp_id = None

	def getapiname(self):
		return 'taobao.opentrade.special.items.unbind'
