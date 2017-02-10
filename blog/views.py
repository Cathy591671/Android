# coding:utf-8
import os
from django import forms
from django. shortcuts import render_to_response
from blog. models import Blog
from django. shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django. contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
# Create your views here.

@login_required
def index(request):
    blog_list = Blog. objects. all()
    username = request.session.get('name', '')
    print 'username'
    print username
    if username:
        return render_to_response('index.html', {'myname': username, 'blogs': blog_list})
    else:
        return render(request, "login.html")


def login(request):
    return render(request, "login.html")


def first(request):
    return render(request, "first.html")


def login_action(request):
    print (request.method)
    username = request.POST.get("username")
    password = request.POST.get("password")
    #users_ = [username]
    user = auth. authenticate(username=username, password=password)
    if user is not None:
        auth. login(request, user)
        response = HttpResponseRedirect('/index/')
        request.session['name'] = username
        return response
    else:
        return render_to_response('login.html', {'error': 'name or password wrong'})

@login_required
def logout(request):
    response = HttpResponseRedirect('/login/')
    del request.session['name']
    return response

#upload
def uploadfile(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile =request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render_to_response('index.html', {'error': 'no fileno'})
            #raise forms.ValidationError(u"请选择要上传的文件")
        destination = open(os.path.join("C:\Users\Cathy\PycharmProjects\connect",myFile.name),'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return render_to_response('index.html', {'upload success'})
        #raise forms.ValidationError(u"上传成功")
