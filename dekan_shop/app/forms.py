from django import forms

class Product(forms.Form):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__input__block__ch', 'name': 'title'}))
    chapter = forms.ChoiceField(choices=((1, 'Ноутбуки'), (2, 'Мыши'), (3, 'Наушники')), label='', widget=forms.Select(attrs={'class': 'form__input__block__ch'}))
    price = forms.IntegerField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'price'}))
    link_img = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'link_img'}))