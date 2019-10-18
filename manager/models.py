from django.db import models
from django import forms
import datetime
# Create your models here.


class Tool(models.Model):
    name = models.CharField(max_length=10, verbose_name="分类名")
    free_tools = models.TextField(verbose_name="可用工具（请用逗号隔开）", default="")
    used_tools = models.TextField(
        verbose_name="已使用工具（请用逗号隔开）", blank=True, default="")
    remark = models.TextField(verbose_name="备注", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "设备管理"


class RentOrder(models.Model):
    name = models.CharField(verbose_name="申请人", max_length=10)
    tools = models.TextField(verbose_name="借用设备")
    regard = models.TextField(verbose_name="借用事由")
    phone = models.IntegerField(verbose_name="电话号码")
    date = models.DateField(verbose_name="借出日期")
    # return_date = models.DateField(
    #     verbose_name="归还日期", blank=True, auto_now=True)
    is_returned = models.BooleanField(verbose_name="是否归还", default=False)

    def __str__(self):
        return self.name+"--"+self.regard

    class Meta:
        verbose_name_plural = "借用订单管理"
