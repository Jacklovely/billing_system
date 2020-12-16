from django.db import models

# Create your models here.

class Users(models.Model):
    user_name =models.CharField('用户名',max_length=64,default='guest',help_text="用户名")#用户名
    password = models.CharField(max_length=64,help_text='密码')#密码
    role = models.CharField(max_length=32,default=2,help_text='用户等级')#0代表超级管理员#1代表普通管理员2代表guest
    register_time = models.DateTimeField(auto_now=True,help_text='注册时间')#注册时间
    login_time = models.CharField(max_length=64,default='Null',help_text='登录时间')
    icon = models.CharField(max_length=64,default='/icon/default.png',help_text='用户头像地址')#用户头像地址
    session = models.CharField(max_length=64,help_text='session')#登录后生成的随机字符串
    comments = models.CharField(max_length=64,default='游客',help_text='备注')
    login_name = models.CharField(max_length=64,default='Null',help_text='登录用户名')

    class Meta:
        db_table = 'users'

    def __unicode__(self):
        return self.user_name

    def __str__(self):
        return self.user_name

class Manage(models.Model):
    id = models.AutoField(primary_key=True,help_text='id')
    account_name = models.CharField(max_length=64,help_text='账目名称')
    type = models.CharField(max_length=64,default=1,help_text='账目类型')#1收入；2消费；3借出；4理财
    income_type = models.CharField(max_length=64,default=1,help_text='收入类型')#1薪资收入；2理财输入；其他收入
    consume_type = models.CharField(max_length=64,default=1,help_text='消费类型')#1生活消费；2出行消费；3还贷消费；4，购物消费；5其他消费
    lend_type = models.CharField(max_length=64,default=1,help_text='借出类型')#1借出；2已还；3未还
    manage_money_type = models.CharField(max_length=64,default=1,help_text='理财类型')#1理财产品；2基金；3其他
    comments = models.CharField(max_length=64, null=True,help_text='备注')  # 备注
    income_time = models.CharField(max_length=32,null=True,help_text='收入时间')
    consume_time = models.CharField(max_length=32,null=True,help_text='消费时间')
    lend_time = models.CharField(max_length=32,null=True,help_text='借出时间')
    manage_money_time = models.CharField(max_length=32,null=True,help_text='理财时间')

    class Meta:
        db_table = 'manage'

    def __unicode__(self):
        return self.account_name

    def __str__(self):
        return self.account_name



