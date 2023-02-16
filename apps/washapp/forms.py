from django import forms
from .models import order_detail

class ODModelForm(forms.ModelForm):
    class Meta:
        model = order_detail
        # fields = '__all__'
        fields = ('washmode', 'spinmode','drymode','foldmode')
        washchoice=((1, "標準(30min)"), (2, "精緻洗(50min)"), (3, "柔洗(40min)"), (4, "快洗(20min)"))
        spinchoice=((1, "脫水"), (2, "不脫水"))
        drychoice=((1, "日曬"), (2, "低溫烘乾"), (3, "中溫烘乾"), (4, "高溫烘乾"))
        foldchoice=((1, "機器人"), (2, "不摺"))
        washmode=forms.ChoiceField(choices=washchoice,initial=washchoice[0])
        spinmode=forms.ChoiceField(choices=spinchoice,initial=spinchoice[0])
        drymode=forms.ChoiceField(choices=drychoice,initial=drychoice[0])
        foldmode=forms.ChoiceField(choices=foldchoice,initial=foldchoice[0])
        widgets = {
            'washmode': forms.Select(choices=washchoice),
            'spinmode': forms.Select(choices=spinchoice),
            'drymode': forms.Select(choices=drychoice),
            'foldmode': forms.Select(choices=foldchoice),
        }