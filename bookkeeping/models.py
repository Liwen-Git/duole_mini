from django.db import models

# Create your models here.
from django.db import models


class BillType(models.Model):
    name = models.CharField(max_length=30, verbose_name='类型名')
    pid = models.IntegerField(verbose_name='上级id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bookkeeping_bill_type'
        verbose_name = '账单类型'
