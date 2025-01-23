from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def index(request):
    title = 'магазин'
    main='главная страница'
    text = 'купить'
    back='на главную'
    context = {'main':main,
               'title': title,
               'text': text,
               'back':back}

    return render(request, 'third_task/1.html',context)


class index2(TemplateView):
    template_name = 'third_task/2.html'

# class index3(TemplateView):
#     template_name='third_task/3.html'
