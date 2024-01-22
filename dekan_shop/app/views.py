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
        product.title = request.POST.get('title', 'Undefined')
        product.path_img = request.POST.get('path_img', 'Undefined')
        product.price = request.POST.get('price', 'Undefined')
        product.input_chapter = request.POST('chapter', 'Undefined')
        product.save()
        if input_chapter == '1':
            notebook.append({"price": price, "title": title, "path_img": path_img})
            Item_Notebook.objects.create(title=title, link_img=link_img, price=price)
        elif input_chapter == '2':
            comp_mouse.append({"price": price, "title": title, "path_img": path_img})
            Item_Comp_Mouse.objects.create(title=title, link_img=link_img, price=price)
        elif input_chapter == '3':
            headphones.append({"price": price, "title": title, "path_img": path_img})
            Item_Headphones.objects.create(title=title, path_img=path_img, price=price)
        return HttpResponseRedirect('/')
    else:
        product = Product()
        return render(request, 'app/Shop_form.html', context={'product': product})
