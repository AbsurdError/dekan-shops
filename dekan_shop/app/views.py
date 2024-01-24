from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
from .models import *
# Create your views here.
def one_page(request):
    notebooks = Item_Notebook.objects.all()
    return render(request, 'app/One_page.html', context={'notebooks': notebooks})

def two_page(request):
    comp_mouses = Item_Comp_Mouse.objects.all()
    return render(request, 'app/Two_page.html', context={'comp_mouses': comp_mouses})

def tree_page(request):
    headphones = Item_Headphones.objects.all()
    return render(request, 'app/Three_page.html', context={'headphones': headphones})

def shop_form(request):
    if request.method == 'POST':
        product = Product()
        title = request.POST.get('title', 'Undefined')
        path_img = request.POST.get('path_img', 'Undefined')
        price = request.POST.get('price', 'Undefined')
        input_chapter = request.POST.get('chapter', 'Undefined')

        if input_chapter == 'Ноутбуки':
            Item_Notebook.objects.create(title=title, path_img=path_img, price=price)
        elif input_chapter == 'Мыши':
            Item_Comp_Mouse.objects.create(title=title, path_img=path_img, price=price)
        elif input_chapter == 'Наушники':
            Item_Headphones.objects.create(title=title, path_img=path_img, price=price)
        return HttpResponseRedirect('/')
    else:
        product = Product()
        return render(request, 'app/Shop_form.html', context={'product': product})
