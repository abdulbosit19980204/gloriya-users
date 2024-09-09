import time
from datetime import timezone, datetime

from django.db.models import Count
from django.shortcuts import render
from django.views.generic import RedirectView
from rest_framework.utils.humanize_datetime import datetime_formats

from auth_app.models import User, MyUser
from django.db import connection
from tracker.views import fetch_data_from_raw_table
from .models import entities, AdditionalSourcesModels
from tracker.models import ChanelModel
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from auth_app.views import client
from currency_converter import CurrencyConverter
from google_currency import convert

c = CurrencyConverter()


def home_view(request):
    data = request.GET
    page = data.get('page', 1)
    visited = AdditionalSourcesModels.objects.filter(author=request.user).first()
    if visited is None:
        visit = AdditionalSourcesModels.objects.create(author=request.user, visitors=1)
        visit.save()
    visited.visitors += 1
    visited.save(update_fields=['visitors'])
    d = {}
    my_user = MyUser.objects.filter(user=request.user).first()
    all_entities = entities.objects.all()
    all_orders = 0
    total_orders_sum = 0
    if my_user.code:
        getOrderList = client.service.GetOrderList(my_user.code)
        if getOrderList:
            getOrderList = client.service.GetOrderList(my_user.code)[::-1]
            d['orders'] = Paginator(getOrderList, 15).get_page(page)

            for i in getOrderList:
                total_orders_sum += i['Total']
                all_orders += 1

    # d['all_entities'] = getOrderList.count()
    d['all_entities'] = all_orders
    d['user'] = my_user
    d['visited'] = AdditionalSourcesModels.objects.filter(author=request.user).first()
    d['total_orders_sum'] = c.convert(total_orders_sum, 'EUR', 'USD')
    return render(request, '../templates/Admin/index.html', context=d)


def user_home_view(request):
    return render(request, '../templates/User/index.html')


def channels_view(request):
    d = {}
    channels = ChanelModel.objects.all()
    d['channels'] = channels
    d['user'] = MyUser.objects.filter(user=request.user).first()
    return render(request, '../templates/Admin/channels.html', context=d)


def users_view(request):
    myuser = MyUser.objects.filter(user=request.user).first()
    d = {}
    print("code", myuser.code)
    if myuser.code is not None:
        clients = client.service.GetClients(myuser.code)
        d['clients'] = clients
    users = MyUser.objects.all()
    d['user'] = MyUser.objects.filter(user=request.user).first()
    d['users'] = users[:10]
    return render(request, '../templates/Admin/users.html', context=d)


def chart_view(request):
    d = {}
    channel = ChanelModel.objects.all().values('username').annotate(count=Count('username'))
    labbels = []
    data = []
    for c in channel:
        labbels.append(c['username'])
        data.append(c['count'])
    d['labbels'] = labbels
    d['labbel'] = "Channels"
    d['data1'] = data
    d['data2'] = data[::-1]
    d['data3'] = data[1:5]

    d['user'] = MyUser.objects.filter(user=request.user).first()
    return render(request, './Admin/chartjs.html', context=d)


def order_detail_view(request, code):
    print(client.service.GetOrderDetails("GL00-170643", '20240813000000', '20240913000000'))


def getWarehouses_view():
    warehouses = client.service.GetWarehouses()
    return warehouses


def getProductBlance_view(CodeProject, CodeSklad):
    productBlance = client.service.GetProductBalance(CodeProject, CodeSklad)
    return productBlance


def getClients_view(UserCode):
    clients = client.service.GetClients(UserCode)
    return clients


def getPriceTypes_view(UserCode):
    priceList = client.service.GetPriceTypes(UserCode)
    return priceList


def getUser_view(request):
    print(request.GET.get('user'))
    user = request.GET.get('user')
    password = request.GET.get('password')
    user_data = client.service.GetUser(user, password)
    wharehouses = getWarehouses_view()
    # print(wharehouses)
    products = getProductBlance_view(user_data['CodeProject'], user_data['CodeSklad'])
    clients = getClients_view(user_data['Code'])
    priceList = getPriceList_view(user_data['Code'])
    print(user_data),
    print(priceList)
    d = {
        "user": user_data,
        "clients": clients,
        "wharehouses": wharehouses,
        "products": products
    }

    return render(request, '../templates/Admin/dist/tables-responsive.html', context=d)


def getRateOfCurrency_view(Code, Data):
    currency_rate_now = client.service.GetRateOfCurrency(Code, Data)


def GetClientBalance(ClientCode, Data):
    clientBlance = client.service.GetClientBalance(ClientCode, Data)
    print(clientBlance)
    return clientBlance


def getPriceList_view(UserCode):
    priceList = client.service.GetPriceList(UserCode)
    return priceList


def checkProductBlance_view(UserCode):
    pass


def getOrderList(CodeAgent):
    pass


def getOrderDetail_view(NumberOrder, OrderDate1, OrderDate2):
    orderDetail = client.service.GetOrderDetails(NumberOrder, OrderDate1, OrderDate2)


def getShippingList_view(UserCode):
    pass


def getBusinessRegions_view(UserCode):
    pass


def getDiscountList_view(UserCode):
    pass


def getReasonOfReturn_view(UserCode):
    pass


def getCashmansList_view(UserCode):
    pass


def getKPI(CodeUser):
    pass


def getDilers():
    pass


def getOrganizations():
    pass


def getWarehousesUser(CodeUser):
    pass


def getContracts(CodeUser, CodeClient):
    pass


def getClientsThroughINN(INN):
    pass


def getBankName(MFO):
    pass
