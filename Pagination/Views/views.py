from django.shortcuts import render
from django.core.paginator import Paginator
from test_01 import models
# Create your views here.

def bashborad(request):
    host_li=models.host.objects.all()

    #��ʼ��ҳ10��models��ѯʵ��Ϊһҳ
    host_li_groups=Paginator(host_li,10)
    page_num=request.GET.get('page')     #��ȡ�û���Ҫ�ĵ�page_numС��

    host_li_group=host_li_groups.get_page(page_num)  #�õ��û���Ҫ�ĵ�page_numС��,2.0ʹ��get_page�������ڲ����쳣
    return  render(request,'pro/dashboard.html',{'host_list':host_li_group,})  #proΪ��Ŀ��