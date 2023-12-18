from django import forms

class InputTitle(forms.Form):
    title = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class': 'form__input__block__ch', 'name': 'title'}))

class InputChapter(forms.Form):
    chapter = forms.ChoiceField(choices=((1, 'Ноутбуки'), (2, 'Мыши'), (3, 'Наушники')), label='', widget=forms.Select(attrs={'class': 'form__input__block__ch'}))

class InputPrice(forms.Form):
    price = forms.IntegerField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'price'}))

class InputLinkImg(forms.Form):
    link_img = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'class':'form__input__block__ch', 'name': 'link_img'}))