'''
Created by auto_sdk on 2021.11.08
'''
from seven_top.top.api.base import RestApi
class MiniappDistributionMaterialUpdateRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.material_request = None

	def getapiname(self):
		return 'taobao.miniapp.distribution.material.update'
