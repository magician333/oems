from django.shortcuts import render, HttpResponse
from manager.models import Tool, RentOrder
# Create your views here.

All = Tool.objects.all()
name = list()
tools = list()
for i in All:
    name.append(i.name)
    tools.append(i.free_tools.split(","))  # 字符串转列表
content = dict(zip(name, tools))  # 做成字典


def index(request):
    return render(request, "index.html", {"content": content})


def rent(request):
    return render(request, "rent.html", {"content": content})


def return_tools(request):
    Orders = RentOrder.objects.all()
    return render(request, "return.html", {"orders": Orders})


def returned(request, order_id):
    # 将是否归还设置为True
    order = RentOrder.objects.get(id=order_id)
    order.is_returned = True
    order.save()
    return render(request, "return_ok.html")


def show_orders(request):
    Orders = RentOrder.objects.all()
    return render(request, "all_orders.html", {"orders": Orders})


def free2used(wtList):
    for i in wtList:
        for j in All:
            if i in j.free_tools:
                # print(j.free_tools.split(","))
                # print(j.free_tools.split(",").index(i))
                j.free_tools.split(",").pop(
                    j.free_tools.split(",").index(i))
                print(j.free_tools.split(","))
        # j.used_tools = i+","+j.used_tools
        # j.save()


def order(request):
    # 提交订单后，将选择的可用设备转换为不可用设备
    ro = RentOrder()
    ro.name = request.POST["name"]
    ro.tools = ",".join(request.POST.getlist("tool"))  # 列表转字符串
    # free2used(request.POST.getlist("tool"))
    ro.regard = request.POST["regard"]
    ro.phone = request.POST["phone"]
    ro.date = request.POST["date"]
    ro.is_returned = False
    ro.save()
    return render(request, "rent_ok.html", {"name": ro.name, "tools": ro.tools})
