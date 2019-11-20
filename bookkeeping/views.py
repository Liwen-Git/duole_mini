from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from bookkeeping.models import BillType
from duole_mini import utils
from bookkeeping.validate import TypeAddValidate


# 分类添加
@csrf_exempt
def type_add(request):
    valid = TypeAddValidate(request.POST)
    if valid.is_valid():
        name = request.POST['name']
        pid = request.POST['pid']

        bill_type = BillType()
        bill_type.name = name
        bill_type.pid = pid
        bill_type.save()

        data_dict = utils.change_to_list_dict(bill_type)
        return utils.success(data_dict)
    else:
        return utils.error(message=valid.errors)


# 分类列表
def type_list(self):
    list_val = BillType.objects.all()
    return_list = utils.change_to_list_dict(list_val)

    return utils.success(return_list)
