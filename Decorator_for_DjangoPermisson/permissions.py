#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.urls import reverse,resolve
from django.shortcuts import render, redirect

# 第一步定义好的动作映射表,下面是范例
perm_dic = {
    'view_task': ['sec_p', 'GET', []],  # 表示可以在url页面进行查看。view_task是在modles中定义的名称
    'edit_task': ['sec_p', 'POST', ['host_name']],  # 表示可以在url页面进行表单提交，但是提交的数据中必须有参数名为host_name。edit_task是在modles中定义的名称
}


# 开始定义装饰器

# 进行动作判断和用户权限判断
def perm_check(*args, **kwargs):
    # 获取当前的动作，然后与映射表的动作进行判断
        request = args[0]
        url_resovle_obj = resolve(request.path_info)  # 获取当前url
        current_url_namespace = url_resovle_obj.url_name  # 获取当前url的别名
        # app_name = url_resovle_obj.app_name #use this name later
        print("url namespace:", current_url_namespace)
        matched_flag = False  # find matched perm item 判断动作匹配成功与否的标识
        matched_perm_key = None  # 判断用户权限成功与否的标识
        if current_url_namespace is not None:  # 如果url别名存在
            print("find perm...")
            for perm_key in perm_dic:  # 开始匹配当前动作的url、请求、参数与映射表中的url、请求、参数
                perm_val = perm_dic[perm_key]
                if len(perm_val) == 3:  # otherwise invalid perm data format
                    url_namespace, request_method, request_args = perm_val
                    print(url_namespace, current_url_namespace)
                    if url_namespace == current_url_namespace:  # matched the url
                        if request.method == request_method:  # matched request method
                            if not request_args:  # if empty , pass
                                matched_flag = True
                                matched_perm_key = perm_key
                                print('mtched...')
                                break  # no need looking for  other perms
                            else:
                                for request_arg in request_args:  # might has many args
                                    request_method_func = getattr(request, request_method)  # get or post mostly
                                    # print("----->>>",request_method_func.get(request_arg))
                                    if request_method_func.get(request_arg) is not None:
                                        matched_flag = True  # the arg in set in perm item must be provided in request data
                                    else:
                                        matched_flag = False
                                        print("request arg [%s] not matched" % request_arg)
                                        break  # no need go further
                                if matched_flag == True:  # means passed permission check ,no need check others
                                    print("--passed permission check--")
                                    matched_perm_key = perm_key
                                    break
        # 当前的动作在映射表里面的动作中都没有时的操作（动作匹配失败），这里默认是运行执行
        else:  # permission doesn't work
            return True

        # 动作匹配成功后，执行用户权限匹配操作
        if matched_flag == True:
            # pass permission check
            # perm_str = "<工程名>.%s" % (matched_perm_key)
            perm_str = "pro.%s" % (matched_perm_key)  # 根据获取到的动作映射表的key生成用户对应的动作key，注意这里的pro是创建权限管理字符串所在的工程名
            if request.user.has_perm(perm_str):
                print("\033[42;1m--------passed permission check----\033[0m")
                return True
            else:
                print("\033[41;1m ----- no permission ----\033[0m")
                print(request.user, perm_str)
                return False
        else:
            print("\033[41;1m ----- no matched permission  ----\033[0m")

# 定义装饰器
def check_perm(func):
    def wrapper(*args, **kwargs):
        print("---start check perms", args[0])
        if not perm_check(*args, **kwargs):  # 调用了动作和用户权限匹配函数
            return render(args[0], 'pro/403.html')
        return func(*args, **kwargs)
        # print("---done check perms")

    return wrapper