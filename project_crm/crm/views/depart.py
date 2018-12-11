from django.shortcuts import render,redirect
from crm  import  models
from crm.forms.depart import DepartModelForm
from crm.views import my_page
import time
def depart_list(request):
    """
    部门列表
    :param request:
    :return:
    """
    # 从url获取页码数，若没有则默认取第一页
    try:
        page_num = request.GET.get("page")
    except Exception as e:
        page_num = 1
    # 获取总数据
    totle_count = models.DepartMent.objects.all().count()
    page = my_page.Page(page_num, totle_count, per_pag=5, url_prefix="/crm/depart/list/", max_page=11)
    depart_queryset = models.DepartMent.objects.all()[page.data_start:page.data_end]
    page_html = page.page_html()
    return render(request,'depart_list.html',{"depart_queryset":depart_queryset,"page_html":page_html})

def depart_add(request):
    if request.method == "GET":
        form = DepartModelForm()
        return render(request, 'depart_form.html', {"form":form})
    form = DepartModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list/')
    return render(request, 'depart_form.html', {"form":form})

def depart_edit(request,nid):
    obj = models.DepartMent.objects.filter(id=nid).first()
    if request.method == "GET":
        form = DepartModelForm(instance=obj)
        return render(request,'depart_form.html',{"form":form})
    form = DepartModelForm(data=request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/crm/depart/list/')
    return render(request,'depart_form.html',{"form":form})

def depart_del(request,nid):
    # time.sleep(1)
    # nid = request.POST.get("id")
    models.DepartMent.objects.filter(id=nid).delete()
    return redirect('/crm/depart/list/')