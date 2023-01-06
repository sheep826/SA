from django import forms
from .models import order_detail
class order_detailModelForm(forms.ModelForm):
    class Meta:
        model = order_detail
        fields = '__all__'