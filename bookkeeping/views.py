from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from bookkeeping.models import BillType
from duole_mini import utils
import json


class BillTypeController(object):
    # 分类添加
    @csrf_exempt
    def type_add(self, request):
        req_dict = json.loads(request.body.decode('utf-8'))
        if not req_dict.get('name'):
            return utils.error('类型名称不能为空')
        elif not req_dict.get('pid'):
            return utils.error('上级不能为空')
        else:
            name = req_dict.get('name')
            pid = req_dict.get('pid')

            bill_type = BillType()
            bill_type.name = name
            bill_type.pid = pid
            bill_type.save()

            data_dict = utils.change_to_list_dict(bill_type)
            return utils.success(data_dict)

    # 编辑分类
    @csrf_exempt
    def type_edit(self, request):
        req_dict = json.loads(request.body.decode('utf-8'))
        if not req_dict.get('name'):
            return utils.error('类型名称不能为空')
        elif not req_dict.get('pid'):
            return utils.error('上级不能为空')
        elif not req_dict.get('id'):
            return utils.error('id不能为空')
        else:
            id = req_dict.get('id')
            name = req_dict.get('name')
            pid = req_dict.get('pid')

            bill_type = BillType.objects.get(pk=id)
            bill_type.name = name
            bill_type.pid = pid
            bill_type.save()

            data_dict = utils.change_to_list_dict(bill_type)
            return utils.success(data_dict)

    # 分类列表
    @staticmethod
    def type_list(self):
        list_val = BillType.objects.all()
        return_list = utils.change_to_list_dict(list_val)

        return utils.success(return_list)

    # 删除
    @csrf_exempt
    def type_delete(self, request):
        req_dict = json.loads(request.body.decode('utf-8'))
        if req_dict.get('id'):
            id = req_dict.get('id')
            bill_type = BillType.objects.get(pk=id)
            count = BillType.objects.filter(pid=bill_type.id).count()
            if bill_type.pid == 0 and count > 0:
                return utils.error(message='该分类存在子类')
            else:
                bill_type.delete()
                return utils.success()
        else:
            return utils.error(message='删除ID不能为空')
