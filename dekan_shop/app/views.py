from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import *
# Create your views here.
def one_page(request):
    data = {'notebook': notebook}
    return render(request, 'app/One_page.html', context=data)

def two_page(request):
    data = {'comp_mouse': comp_mouse}
    return render(request, 'app/Two_page.html', context=data)

def tree_page(request):
    data = {'headphones': headphones}
    return render(request, 'app/Three_page.html', context=data)

def shop_form(request):
    if request.method == 'POST':
        title = request.POST.get('title', 'Undefined')
        link_img = request.POST.get('link_img', 'Undefined')
        price = request.POST.get('price', 'Undefined')
        input_chapter = InputChapter(request.POST)
        if input_chapter.is_valid():
            chapter = input_chapter.cleaned_data['chapter']
        if chapter == '1':
            notebook.append({"price": price, "title": title, "link_img": link_img})
        elif chapter == '2':
            comp_mouse.append({"price": price, "title": title, "link_img": link_img})
        elif chapter == '3':
            headphones.append({"price": price, "title": title, "link_img": link_img})
        return HttpResponseRedirect('/')
    else:
        input_title = InputTitle()
        input_chapter = InputChapter()
        input_link_img = InputLinkImg()
        input_price = InputPrice()
        return render(request, 'app/Shop_form.html', context={'input_title': input_title, 'input_price': input_price, 'input_link_img': input_link_img, 'input_chapter': input_chapter})


notebook = [
    {'price': '34 999', 'title': '15.6" Ноутбук MSI Modern 15 B11M-003XRU черный [Full HD (1920x1080), IPS, Intel Core i3-1115G4, ядра: 2 х 3 ГГц, RAM 8 ГБ, SSD 256 ГБ, Intel UHD Graphics , без ОС]', 'link_img': 'https://c.dns-shop.ru/thumb/st1/fit/500/500/ff631e895a39d034a660c0f55380505c/e24fceb75e19fec7069e3cfdaa01a8e337487b4bf99b4cac807c6c19ad36284c.jpg.webp'},
    {'price': '35 999', 'title': '15.6" Ноутбук ASUS ExpertBook B1502CGA-BQ0084X черный [Full HD (1920x1080), IPS, Intel Processor N100, + 4, RAM 4 ГБ, SSD 128 ГБ, Intel UHD Graphics , Windows 11 Pro]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/f2a44595f24ad8e4f719574565307e04/9f043b2d0bcf0c845d1422dffa229bfa09711be8180262d765de1cb237b45b1a.jpg.webp'},
    {'price': '71 999', 'title': '15.6" Ноутбук ARDOR GAMING NEO G15-I5ND300 черный [Full HD (1920x1080), IPS, Intel Core i5-12450H, ядра: 4 + 4 х 2 ГГц, RAM 16 ГБ, SSD 512 ГБ, GeForce RTX 3050 для ноутбуков 6 ГБ, без ОС]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/200/200/14c21552e8e089589a44c82ee97a9781/a679933bd6cdf9d9db67a738aefc14292313766793cb541f401d6c826239b053.jpg.webp'},
]

comp_mouse = [
    {'price': '2 699', 'title': 'Мышь проводная ARDOR GAMING Agile [ARD-AG3389-WT] белый [16000 dpi, светодиодный, USB Type-A, кнопки - 6]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/e5ef71d4638d54b61aa1127062a46a4d/8a208f413f689ba27050a94619c71365827d7557bc612b4f8d83d3c043f08d4a.jpg.webp'},
    {'price': '4 299', 'title': 'Мышь проводная HyperX Pulsefire Haste [4P5P9AA] черный [16000 dpi, светодиодный, USB Type-A, кнопки - 6]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/8c126f045652b9f9cf42e64100105de4/492e3961a15d97ae18daeb540a69f7e4a6259efbe0939185214a4c6934a9facc.jpg.webp'},
    {'price': '4 699', 'title': 'Мышь проводная Razer Cobra [RZ01-04650100-R3M1] черный [8500 dpi, светодиодный, USB Type-A, кнопки - 6]', 'link_img': 'https://c.dns-shop.ru/thumb/st1/fit/500/500/f13a2f82d5181c0684811c9e56d04666/be48e03962dd073f0027650b5840263976f528cd9bba5506807044ae941065fb.jpg.webp'},
]

headphones = [
    {'price': '5 099', "title": 'Проводная гарнитура HyperX Cloud Stinger 2 Core белый [2.0, поддержка PS4, PS5, охватывающие, 10 Гц - 25000 Гц, проводной, кабель - 1.3 м]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/d7ccfef128df84f77143af58d4e63ea5/98312eb16806a099457576c6343726e8b90babaf9200f52b5578404301abe396.jpg.webp'},
    {'price': '5 099', "title": 'Проводная гарнитура Razer Kraken V3 X черный [7.1 Virtual, охватывающие, 12 Гц - 28000 Гц, 32Ω, проводной, кабель - 1.8 м]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/d769dc8f35e4a050b8b1d8e53684c37b/b8304a1dbab2af4153e9eb00667acdee1761c7033b4d2ed5c6926e750a535ae7.jpg.webp'},
    {'price': '5 199', "title": 'Радиочастотная гарнитура ARDOR GAMING Vault черный [7.1 Virtual, охватывающие, 20 Гц - 20000 Гц, 64Ω, Bluetooth, проводной, радиоканал, 5.2, кабель - 1.8 м]', 'link_img': 'https://c.dns-shop.ru/thumb/st4/fit/500/500/a17d7b0a8d1c869c0e1c7af30ecb70de/f78f4f33e6e8296cb00011bfc0c4d15d60fcb21cedd5c5320baf9ee5e4b92fb5.jpg.webp'},
]