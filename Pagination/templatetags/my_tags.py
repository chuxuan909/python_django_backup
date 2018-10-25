#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django import template
register = template.Library()

from django.utils.html import format_html   #此模块用于将返回的html代码字符串转化为template识别的html代码


@register.simple_tag
def display_page(current_page, loop_page):
    offset = abs(current_page - loop_page)  # 当前页和循环页的差距

    # 当差距小于3时，显示出循环页的页码
    if offset < 3:
        if current_page == loop_page:  # 循环页和当前页相同时显示的html代码
            page_html = '''<li class="active" ><a href="?page=%s">%s<span class="sr-only">(current)</span></a></li>''' % (
            loop_page, loop_page)
        else:  # 循环页和当前页不相同时显示的html代码
            page_html = '''<li class="" ><a href="?page=%s">%s<span class="sr-only">(current)</span></a></li>''' % (
            loop_page, loop_page)
        return format_html(page_html)  # 转化html代码字符串为html代码，否则模板html不识别
    # 当差距大于3时，显示空白，函数一定要有返回值，不然会返回none显示在页面
    else:
        return ''