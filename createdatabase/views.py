from django.shortcuts import render,HttpResponse

# Create your views here.
from createdatabase import models


def createdatabase(request):
    #开始创建数据库
    models.Users.objects.create(user_name='admin',
                                login_name='admin',
                                password='admin',
                                role=0,
                                register_time='',
                                login_time='',
                                icon='',
                                session='',
                                comments='超级管理员')
    return HttpResponse('create database succeed !')

def test(request):
    manageobj = models.Manage.objects.filter(**{})

    print(manageobj)

    return HttpResponse('ok')
