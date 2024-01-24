from django import forms

class Product(forms.Form):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__input__block__ch', 'name': 'title'}))
    chapter = forms.ChoiceField(choices=(('Ноутбуки', 'Ноутбуки'), ('Мыши', 'Мыши'), ('Наушники', 'Наушники')), label='', widget=forms.Select(attrs={'class': 'form__input__block__ch'}))
    price = forms.IntegerField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'price'}))
    path_img = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'path_img'}))