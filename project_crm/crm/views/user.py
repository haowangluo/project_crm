from django.shortcuts import render,redirect
from crm import models
from crm.forms.user import UserModelForm
from crm.views import my_page
def user_list(request):
    # 从url获取页码数，若没有则默认取第一页
    try:
        page_num = request.GET.get("page")
    except Exception as e:
        page_num = 1
    # 获取总数据
    totle_count = models.UserInfo.objects.all().count()
    page = my_page.Page(page_num, totle_count, per_pag=5, url_prefix="/crm/user/list/", max_page=11)
    user_queryset = models.UserInfo.objects.all()[page.data_start:page.data_end]
    page_html = page.page_html()
    return render(request,'user_list.html',{"user_queryset":user_queryset,"page_html":page_html})

def user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_form.html', {"form":form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return  redirect('/crm/user/list/')
    return render(request, 'user_form.html', {"form":form})

def user_edit(request,nid):
    obj = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=obj)
        return render(request, 'user_form.html', {"form":form})
    form = UserModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/user/list/')
    return render(request, 'user_form.html', {"form":form})

def user_del(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/crm/user/list/')