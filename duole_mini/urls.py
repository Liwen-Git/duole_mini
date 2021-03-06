"""duole_mini URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookkeeping.views import BillTypeController

urlpatterns = [
    path('admin/', admin.site.urls),

    path('bookkeeping/bill_type/add', BillTypeController().type_add),
    path('bookkeeping/bill_type/edit', BillTypeController().type_edit),
    path('bookkeeping/bill_type/list', BillTypeController.type_list),
    path('bookkeeping/bill_type/delete', BillTypeController().type_delete),
]
