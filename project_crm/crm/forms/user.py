from django import  forms
from  crm import  models
class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        widgets = {
            'username':forms.TextInput(attrs={"class":"form-control","placeholder":"用户名"}),
            'password':forms.TextInput(attrs={"class":"form-control","placeholder":"密码"}),
            'email':forms.EmailInput(attrs={"class":"form-control","placeholder":"邮箱"}),
            'gender':forms.Select(attrs={"class":"form-control"}),
            'depart':forms.Select(attrs={"class":"form-control","placeholder":"所在部门"}),
        }
        error_messages = {
            'username': {
                'required': '用户名不能为空'
            },
            'password': {
                'required': '密码不能为空'
            },
            'email': {
                'required': '邮箱不能为空',
                'invalid':'邮箱格式不正确',
            },
            'gender': {
                'required': '请选择性别'
            },
            'depart': {
                'required': '请选择部门'
            },
        }