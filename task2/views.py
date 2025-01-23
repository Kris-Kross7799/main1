from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'second_task/Это шаблон для функционального представления.html')

# class index2(TemplateView):
#     template_name = 'second_task/Это шаблон для классового представления.html'



#python manage.py runserver
