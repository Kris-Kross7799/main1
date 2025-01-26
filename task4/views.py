from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    main="ГЛАВНАЯ СТРАНИЦА"
    backet='корзина'
    text='какой-то текст'
    game='игры'
    shop='shop'
    context = {'games': ['Atomic Heart','Cyberpunk 2077'],
               'pages':[main,game,backet],
               'main':main,
               'backet': backet,
               'text':text,
               'shop':shop}
    return render(request, 'four_task/main.html', context)

def index2(request):
    context = {'games': ['Atomic Heart','Cyberpunk 2077', 'PayDay 2']}

    return render(request, 'four_task/shop.html', context)

def index3(request):
    return render(request, 'four_task/basket.html')

# class index2(TemplateView):
#     template_name = 'four_task/shop.html'

# class index3(TemplateView):
#     template_name='four_task/basket.html'


