'''
Created by auto_sdk on 2022.01.19
'''
from seven_top.top.api.base import RestApi
class MiniappWidgetTemplateInstanceQueryRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.param0 = None

	def getapiname(self):
		return 'taobao.miniapp.widget.template.instance.query'
