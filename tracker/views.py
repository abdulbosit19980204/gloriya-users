from django.shortcuts import render, HttpResponse, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ChannelSerializer
from .models import ChanelModel
import json
from django.db import connection
from dashboard.models import entities
from datetime import datetime

import zeep
from zeep import settings
from zeep.plugins import HistoryPlugin
from zeep import Client, Settings
from zeep.transports import Transport
from lxml import etree
from datetime import datetime as dt

settings = Settings(strict=False, xml_huge_tree=True)
history = HistoryPlugin()
transport = Transport(timeout=10)
reasionsReturn = 'http://kit.gloriya.uz:5443/EVYAP_UT/EVYAP_UT.1cws?wsdl'
client = Client(wsdl=reasionsReturn, transport=transport, plugins=[history], settings=settings)


@api_view(['GET'])
def tracker_view(request):
    channels = ChannelSerializer(ChanelModel.objects.filter(is_synced=False).values_list('username', flat=True))

    return Response(
        data={'channels': channels},
        status=status.HTTP_200_OK
    )


def load_data_view(request):
    fetch_data_from_raw_table()
    return redirect('/')


def add_chanel_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        channel = ChanelModel.objects.create(username=username)
        channel.save()
    return redirect('/channels')


def fetch_data_from_raw_table():
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT id, hash, username, phone, name, date FROM  entities")
        # "SELECT id, hash, username, phone, name, date FROM  entities Where phone=998999992334")
        rows = cursor.fetchall()
        results = []
        for row in rows:
            result = {
                'telegram_id': row[0],
                'hash': row[1],
                'username': row[2],
                'phone': row[3],
                'name': row[4],
                'date': datetime.fromtimestamp(row[5]),
                # Map the rest of your columns
            }
            print(row)
            if entities.objects.filter(hash=result['hash']).exists():
                continue
            dash_entities = entities.objects.create(**result)
            dash_entities.save()
            results.append(result)
            print(result)
    return results

# INSERT INTO dashboard_entities (hash, username, phone, name, date, telegram_id)
# SELECT hash, username, phone, name, date, id
# FROM entities;
