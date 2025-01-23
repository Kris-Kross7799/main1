"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task3.views import index, index2
from django.views.generic import TemplateView

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', index),
#     # path('index2/',index2.as_view()
#     path('class/',TemplateView.as_view(template_name='second_task/Это шаблон для классового представления.html'))] #сгенерировали класс
                                                                                                                    # и получили доступ к его
                                                                                                                    # методу на ходу,                                                                                                            # без создания класса во view
#index2.as_view() - станд.метод класса, который запустит ф-цию,
# аналогичную index(return render(request...)
#можно использовать запись:TemplateView.as_view(template_name=...)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('2/',index2.as_view()),
    path('3/',TemplateView.as_view(template_name='third_task/3.html'))
]
