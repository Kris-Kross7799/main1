from django.shortcuts import render
from django.http import HttpResponse
from task5.forms import UserRegister

users = ['Nikita', 'Oleg', 'Vadim', 'Gektor']
html_path = 'fifth_task/registration_page.html'


# Create your views here.
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            # обработка данных формы:
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            print(f"Name:{username}")
            print(f"Password:{password}")
            print(f"Repeat_password:{repeat_password}")
            print(f"Age:{age}")

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
                return render(request, html_path, context=info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет!'
                return render(request, html_path, context=info)
            elif username in users:
                info['error'] = 'Пользователь с таким логином уже существует!'
                return render(request, html_path, context=info)
            else:
                info['welcome_message'] = 'Приветствуем Вас, {username}!'
            return HttpResponse(f'Приветствуем Вас, {username}!')
    else:
        form = UserRegister()
    return render(request, html_path, {'form': form})


# ----------------------------------------------------------------------------------------------

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        # получаем данные:
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        print(f"Name:{username}")
        print(f"Password:{password}")
        print(f"Repeat_password:{repeat_password}")
        print(f"Age:{age}")

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают!'
            print(info)
            return render(request, html_path, context=info)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет!'
            print(info)
            return render(request, html_path, context=info)
        elif username in users:
            info['error'] = 'Пользователь с таким логином уже существует!'
            print(info)
            return render(request, html_path, context=info)
        else:
            info['welcome_message'] = 'Приветствуем Вас, {username}!'
            # return render(request, html_path, context=info)
            print(info)
            return HttpResponse(f'Приветствуем Вас, {username}!')

    # Если это не GET:
    return render(request, html_path)

# def simple_post(request):
#     if request.method == 'POST':
#         message = request.POST.get("message", "")
#         return HttpResponse(f"You said: {message}")
#     return render(request, 'fifth_task/registration_page.html')

# def index2(request):
#     return HttpResponse('Hi!', status=400, reason='Boom!')

#python manage.py runserver