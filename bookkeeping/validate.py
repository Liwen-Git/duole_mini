from django import forms


class TypeAddValidate(forms.Form):
    name = forms.CharField(max_length=30, required=True, error_messages={'required': '分类名不能为空'})
    pid = forms.IntegerField(min_value=0, required=True, error_messages={'required': '父id不能为空'})


class TypeEditValidate(forms.Form):
    id = forms.IntegerField(min_value=1, required=True, error_messages={'required': 'id不能为空'})
    name = forms.CharField(max_length=30, required=True, error_messages={'required': '分类名不能为空'})
    pid = forms.IntegerField(min_value=0, required=True, error_messages={'required': '父id不能为空'})
