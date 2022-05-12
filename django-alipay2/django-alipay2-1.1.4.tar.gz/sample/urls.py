from django.conf.urls import url
from django.views.generic import TemplateView

from alipay.views import AlipayCallbackView
from .views import example_alipay_create_view

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='sample/samples.html')),
    url(r'^pay/create$', example_alipay_create_view, name='sample_pay_create'),

    url('^callback/$', AlipayCallbackView.as_view(), name='alipay_callback'),
]
