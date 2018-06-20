from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from chat.models import Room
from quiz.models import Result
import django.utils.timezone
from datetime import timedelta
from django.db.models import Max

def index(request):
    # Render that in the index template
    if request.user.is_authenticated:
        rooms = Room.objects.order_by("title")
        result = Result.objects.filter(user_id = request.user)

        start_date = django.utils.timezone.now().date()
        end_date = start_date + timedelta( days=1 )
        max_result = Result.objects.filter(date__range=[start_date, end_date]).aggregate(Max('result'))['result__max']

        ranker = Result.objects.filter(result = max_result).first()
        # ranker = Result.objects.filter(result=score.value())
        return render(request, "login-index.html",{
            "rooms": rooms,
            "result": result,
            "ranker": ranker
        })

    else :
        return render(request, "index.html")




def join(request):

    if request.method == 'POST':
        signup_form = UserForm(request.POST)
        # 유효성 검증에 통과한 경우 (username의 중복과 password1, 2의 일치 여부)
        if signup_form.is_valid():
            # SignupForm의 인스턴스 메서드인 signup() 실행, 유저 생성
            signup_form.signup
            return redirect('index')
    else:
        signup_form = UserForm()

    context = {
        'signup_form': signup_form,
    }
    return render(request, 'registration/adduser.html', context)

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'registration/login.html', {'form': form})

