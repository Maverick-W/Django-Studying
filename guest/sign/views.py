from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event

@csrf_exempt  #申请表单处理
# Create your views here.
def index(request):
    return render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)  #登录
            #response.set_cookie('user',username, 3600)  #添加浏览器cookie
            request.session['user'] = username #将session 信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()  #导入Model的Event类，通过Event.objects.all()查询所有发布会对象
    #username = request.COOKIES.get('user','')  #读取浏览器cookies
    username = request.session.get('user', '')  #读取浏览器session
    return render(request,"event_manage.html",{'user': username,
                                               'event':event_list})
