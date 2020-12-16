# Create your views here.
#引入python core包
import os
import json
from datetime import datetime
#引入django包
from django.shortcuts import render
from billing_manage.forms import SignUpForm
#项目包
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
            wlog('')

#记录日志
def wlog(message):
    logfile = open(file_path,'a+',encoding='utf-8')
    logfile.seek(0)
    logLineNum = len(logfile.readlines())
    if logLineNum<50:
        logfile.write(datetime.now)