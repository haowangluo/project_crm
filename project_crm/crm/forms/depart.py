from crm  import  models
from django.forms import ModelForm
from django import  forms
class DepartModelForm(ModelForm):
    class Meta:
        model = models.DepartMent
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'部门名称'})
        }
        error_messages = {
            'title':{
                'required':'部门名称不能为空'
            }
        }