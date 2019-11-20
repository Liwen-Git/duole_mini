from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from bookkeeping.models import BillType
from django.forms.models import model_to_dict
from duole_mini import utils


@csrf_exempt
def add(request):
    name = request.POST['name']
    pid = request.POST['pid']

    bill_type = BillType()
    bill_type.name = name
    bill_type.pid = pid
    bill_type.save()

    data_dict = utils.change_to_list_dict(bill_type)
    return utils.success(data_dict)


def get_list(self):
    list_val = BillType.objects.all()
    return_list = utils.change_to_list_dict(list_val)

    return utils.success(return_list)


