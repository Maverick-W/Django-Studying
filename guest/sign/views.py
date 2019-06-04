from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


@csrf_exempt  #申请表单处理
# Create your views here.
def index(request):
    return render(request,"index.html")

#登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username == 'admin' and password == 'admin123':
            response = HttpResponseRedirect('/event_manage/')
            response.set_cookie('user',username, 3600)  #添加浏览器cookie
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

#发布会管理
def event_manage(request):
    username = request.COOKIES.get('user','')  #读取浏览器cookies
    return render(request,"event_manage.html",{'user': username})
