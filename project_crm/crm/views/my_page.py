from django.shortcuts import render, redirect, HttpResponse
from crm import models
class Page(object):
    def __init__(self,page_num,totle_count,url_prefix,per_pag=2,max_page=11):
        self.url_prefix = url_prefix
        self.max_page = max_page
        # 算出总共需要多少页码来展示数据
        totle_page, m = divmod(totle_count, per_pag)
        if m:
            totle_page += 1
        self.totle_page = totle_page
        # 如果总的页码数超过了最大页码数，默认返回最后一页，当输入的密码不是正经数字，则返回第一页
        try:
            page_num = int(page_num)
            if page_num > totle_page:
                page_num = totle_page
        except Exception as e:
            page_num = 1
        self.page_num = page_num
        # 定义数据从哪取到哪
        self.data_start = (page_num - 1) * per_pag
        self.data_end = page_num * per_pag
        half_max_page = self.max_page // per_pag
        # 页面上的数据页也从哪开始
        page_start = page_num - half_max_page
        # 页面上的数据页从哪结束
        page_end = page_num + half_max_page
        # 如果总页码数小于最大页码数，则最大页码数等于总页码数
        if totle_page < self.max_page:
            self.max_page = totle_page
            # 如果当前页减一半比1小
        if page_start <= 1:
            page_start = 1
            page_end = self.max_page
        # 如果当前页加一半比总页码还大
        if page_end >= totle_page:
            page_end = totle_page
            page_start = totle_page - self.max_page + 1
        self.page_start = page_start
        self.page_end = page_end
    @property
    def start(self):
        return self.data_start
    @property
    def end(self):
        return self.data_end
    def page_html(self):
        # 自己拼接分页的HTML页码
        html_str_list = []
        # 加上第一页
        html_str_list.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix))
        # 上一页 如果第一页 就没有上一页
        if self.page_num <= 1:
            html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            html_str_list.append(
                '<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.url_prefix,self.page_num - 1))
        for i in range(self.page_start, self.page_end + 1):
            # 如果是当前页就加active类
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix,i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix,i)
            html_str_list.append(tmp)
        # 下一页
        if self.page_num >= self.totle_page:
            html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_str_list.append(
                '<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(self.url_prefix,self.page_num + 1))
        # 加最后一页
        html_str_list.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix,self.totle_page))
        page_html = "".join(html_str_list)
        return page_html