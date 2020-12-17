# Create your views here.
#引入python core包
import os
import json
from datetime import datetime
#引入django包
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
#项目包
from billing_manage.forms import SignUpForm, LoginForm
from billing_system.settings import BASE_LOG_DIR
from createdatabase import models

#注册
def signup(request):
    if request.method == 'GET':
        signupform = SignUpForm()
        return render(request,'signup.html',{'signup_form':signupform})
    elif request.method == 'POST':
        signupform = SignUpForm(request.POST)
        username = request.POST.get('user_name')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')

        user_exist = models.objects.filter(user_name = username)
        #判断用户是否已存在
        if user_exist:
            return render(request,'signup.html',{'signup_form':signupform,'error_message':'用户名不能为空'})
        elif password !=repassword:
            return render(request,'signup.html',{'signup_form':signupform,'error_message':'两次输入密码不一致'})
        #提交数据到数据库
        elif signupform.is_valid():
            signupform.cleaned_data.pop('repassword')
            models.Users.objects.create(**signupform.cleaned_data)
            request.session['username'] = username
            request.session['is_login'] = True
            wlog('恭喜' + username + '，注册成功，成为系统用户！\n')
            return redirect('/billing_manage/index/0-0-0-0-0-0/1')
    else:
        signupform = SignUpForm()
        return render(request,'signup.html',{'signup_form':signupform})

# 登录
@csrf_protect
def login(request):
    if request.method == 'GET':
        lf =LoginForm()
        return render(request,'login.html',{'login_form':lf})
    elif request.method == 'POST':
        lf = LoginForm(request.POST)
        username = request.get['user_name']
        password = request.get['password']
        userobj = models.Users.objects.all().filter(user_name=username,password=password)
        if userobj:
            login_name = models.Users.objects.all().filter(user_name=username).values('login_name').first()
            request.session['username'] = login_name['login_name']
            request.session['is_login'] =True
            wlog('欢迎系统用户' + login_name['login_name'] + '登录系统!\n')
            return redirect('/billing_manage/index/0-0-0-0-0-0/1')
        else:
            return render(request,'login.html',{'error_message':'用户名或密码错误','login_form':lf})
    else:
        lf = LoginForm()
        return render(request,'login.html',{'login_form':lf})






file_path = BASE_LOG_DIR+'/logread.log'
#记录日志
def wlog(message):
    logfile = open(file_path,'a+',encoding='utf-8')
    logfile.seek(0)
    logLineNum = len(logfile.readlines())
    if logLineNum<50:
        logfile.write(datetime.now().strftime('%Y-%m-%d %H:%M:%s')+'----->'+message)
        if logLineNum ==49:
            logfile.close()
            save_old_file = file_path+'.'+datetime.now().strftime('%Y-%m-%d')
            os.remove(file_path,save_old_file)
            logfile = open(file_path,'a+')
            logfile.close()
#读取日志
def rlog():
    logfile = open(file_path,'r',encoding='utf-8')
    log_dic = {}
    for key,value in enumerate(logfile,start=1):
        log_dic[key] = value
    return sorted(log_dic.items,key=lambda item:item[0],reverse=True)
