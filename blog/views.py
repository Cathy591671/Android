# coding:utf-8
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
    return render_to_response('index.html', {'myname': username, 'blogs': blog_list})


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

