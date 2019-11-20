# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json


# 返回码
class HttpCode:
    Success = 0
    Error = -1


# 返回成功
def success(data=None, message='OK'):
    json_dict = {
        'code': HttpCode.Success,
        'message': message,
        'data': data,
    }
    json_data = json.dumps(json_dict)
    return HttpResponse(json_data, content_type="application/json")


# 返回失败
def error(data=None, message='ERROR'):
    json_dict = {
        'code': HttpCode.Error,
        'message': message,
        'data': data,
    }
    json_data = json.dumps(json_dict)
    return HttpResponse(json_data, content_type="application/json")


# model 转 json
def model_to_json(data):
    data_dict = model_to_dict(data)
    data_json = json.dumps(data_dict)
    return data_json


# queryset 转 json
def queryset_to_json(data):
    data_json = serializers.serialize('json', list(data))
    return data_json


# valuesqueryset 转 json
def values_queryset_to_json(data):
    data_json = json.dumps(list(data))
    return data_json


# <QuerySet [{'xx': 'xx'},...]> to [{'xx': 'xx'},...]
def values_queryset_to_list_dict(data):
    return list(data)


# <QuerySet [<Model: xxx>,...]> to [{'xxx': 'xxx'},...]
def queryset_to_list_dict(data):
    return_list = []
    for i in data:
        return_list.append(model_to_dict(i))
    return return_list
