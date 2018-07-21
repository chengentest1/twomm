import os
from cmdb import models
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
# Create your views here.
# 1 root 123
# 2 alax 123
# 3 rite 123
# def login(request):
#     if request.method=="GET":
#         return render(request,'login.html')
#     if request.method == "POST":
#         u=request.POST.get('user')
#         p=request.POST.get('pwd')
#         obj=models.UserInfo.objects.filter(username=u,password=p)
#         print(obj)
def login(request):
    # models.UserGroup.objects.create(caption='DBA')

    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # return render(request, 'login.html')
        # # 数据库中执行 select * from user where usernam='x' and password='x'
        u = request.POST.get('user')
        p = request.POST.get('pwd')
        obj = models.UserInfo.objects.filter(username=u, password=p).first()
        if obj:
            return redirect('/cmdb/index/')
        else:
            return render(request, 'login.html')
def index(request):

    return render(request,'index.html')
def user_info(request):
    if request.method=='GET':
        user_list = models.UserInfo.objects.all()
        return render(request, 'user_info.html',{'user_list':user_list})
    elif request.method=='POST':
        u=request.POST.get('user')
        p=request.POST.get('pwd')
        models.UserInfo.objects.create(username=u,password=p)
        user_list=models.UserInfo.objects.all()
        return render(request,'user_info.html',{'user_list':user_list})
def user_detail(request,nid):
    obj=models.UserInfo.objects.filter(id=nid).first()#取单条数据
    return render(request,'user_detail.html',{'obj':obj})
def user_del(requset,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/cmdb/user_info/')
def user_edit(request,nid):
    if request.method=='GET':
        obj=models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_edit.html',{'obj':obj})# obj = models.UserInfo.objects.filter(id=nid).first()
                                                                     # return render(request, 'user_edit.html', {'obj': obj})
    elif request.method=='POST':
        nid=request.POST.get('id')
        u=request.POST.get('username')
        p=request.POST.get('password')
        models.UserInfo.objects.filter(id=nid).update(username=u,password=p)
        return redirect('/cmdb/user_info/')
class Home(View):

    def get(self,request):
        return render(request,'home.html')
    def post(self,request):
        pass

def orm(request):
    result=models.UserInfo.objects.all()
    for row in result:

        print(row.id,row.username,row.password)
    # models.UserInfo.objects.create(
    #     username='rite',
    #     password='123'
    # )
    # return HttpResponse('orm')
# USER_LIST=[
#     {"name":"root"},
# ]

