from django.shortcuts import render
from django.core.paginator import Paginator
from pro import models
# Create your views here.

def bashborad(request):
    host_li=models.host.objects.all()

    #开始分页10个models查询实例为一页
    host_li_groups=Paginator(host_li,10)
    page_num=request.GET.get('page')     #获取用户想要的第page_num小组

    host_li_group=host_li_groups.get_page(page_num)  #拿到用户想要的第page_num小组,2.0使用get_page方法不在捕获异常
    return  render(request,'pro/dashboard.html',{'host_list':host_li_group,})  #pro为项目名
