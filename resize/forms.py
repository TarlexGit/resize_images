from django import forms
from .models import Image_model


class AddImageForm(forms.ModelForm): 
    url = forms.URLField(required=False)
    image_file = forms.ImageField(max_length=50, required=False)
    class Meta:
        model = Image_model
        fields = '__all__'

class ResizeImage(forms.Form):
    width = forms.IntegerField(label='width')
    height = forms.IntegerField(label='height')