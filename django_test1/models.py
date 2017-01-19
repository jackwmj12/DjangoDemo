from django.db import models
from mongoengine import *
from mongoengine import connect
# connect('金属价格', host='192.168.1.115', username='LCC', password='Xyq107995')
connect('金属价格', host='localhost',port=27017)
# Create your models here.
class ArtiInfo(Document):
    date = StringField()
    aluminium_price = StringField()
    num = StringField()
    coper_price = StringField()
    url = StringField()
    index = StringField()
    meta ={
        'collection':"coper.price_info"
    }

class IpInfo(Document):
    ip = StringField()
    num =StringField()
    index =StringField()
    name =StringField()
    meta = {
        'collection': "coper.ip"
    }
# print(ArtiInfo.objects[0].date,ArtiInfo.objects[0].coper_price)
# print(type(ArtiInfo.objects))
# for i in ArtiInfo.objects:
#     print(i.date)