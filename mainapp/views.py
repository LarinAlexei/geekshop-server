from django.shortcuts import render

# Create your views here.

links_menu = [
    {'href': 'products_all', 'name': 'все'},
    {'href': 'products_home', 'name': 'дом'},
    {'href': 'products_office', 'name': 'офис'},
    {'href': 'products_modern', 'name': 'модерн'},
    {'href': 'products_classic', 'name': 'классика'},

]

menu_main = [
    {'menu_session': 'main', 'name': 'Главная'},
    {'menu_session': 'products', 'name': 'Продукты'},
    {'menu_session': 'contact', 'name': 'Контакты'},

]

def main(request):
    content = {
        'title': 'Главная',
        'menu_main': menu_main,
    }
    return render(request, 'mainapp/index.html', content)

def products(request):
    content = {
        'title': 'Товары',
        'links_menu': links_menu,
        'menu_main': menu_main,
    }
    return  render(request, 'mainapp/products.html', content)

def contact(request):
    content = {
        'title': 'Контакты',
        'menu_main': menu_main,
    }
    return  render(request, 'mainapp/contact.html', content)

def context(request):
    content = {
        "title": "подобие ikea",
        "header": "Доброго времени суток",
        "username": "Главный генеральный директор: Ларина Е.В.",
        "products": [
            {"name": "Стулья", "price": 5600},
            {"name": "Пуфы", "price": 3200},
            {"name": "Кровати", "price": 12900},
            {"name": "Диваны", "price": 82700},
        ]
    }

    return render(request, "mainapp/context.html", content)