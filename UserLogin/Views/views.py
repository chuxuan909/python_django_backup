#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
# Create your views here.

@login_required
def index(request):
    return  render(request,'pro/index.html')

def userlogin(request):
    if request.method=='POST':
        user=authenticate(username=request.POST.get('username'),password=request.POST.get('psd')) #验证表单提交过来的用户名和密码
        if user is not None:       #验证成功的操作
            login(request,user)    #验证成功后必须进行的操作，此方法表示登陆成功后，生成session
            return redirect('/pro')           #进行跳转,跳转到'' URL
        else:                  #验证失败的操作,建议跳转到登陆页面，并且在登陆页面的Template上进行一个条件判断
                               #判断如果出现'login_fail'替换标识，则显示标识替换的字符串
            return  render(request,'pro/login.html',{'login_fail':'登陆失败'})
    return render(request, 'pro/login.html')

def userlogout(request):
    logout(request)  #用户退出方法，删除session
    # return HttpResponse('退出成功')
    return redirect('/pro')