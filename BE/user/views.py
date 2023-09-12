from django.shortcuts import render, redirect
from django.db import transaction
from .models import User
from argon2 import PasswordHasher
from .forms import JoinForm, LoginForm
from django.db import IntegrityError

# Create your views here.

# 홈
def index(request):
    context = {}
    login_session = request.session.get('login_session','')
    if login_session == '':
        login_session= False
        context={'login_session':login_session}
        return render(request, 'Project/intro.html', context)
    else:
        login_session=True
        id=request.session['login_session']
        user=User.objects.get(username=id)
        user=user.id
        context={'login_session':login_session,
                 'user':user}
        return render(request, 'Project/intro.html', context)
    

# 회원가입
def join(request):
    joinform = JoinForm
    context = {'forms' : joinform}
    if request.method == 'GET':
        return render(request, 'Project/join.html', context)
    
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        start_period = request.POST.get('start_period', '')
        end_period = request.POST.get('end_period', '')

        joinform = JoinForm(request.POST)
        if password1 != password2:
            return redirect('/accounts/join')
        # elif IntegrityError:
        #     return redirect('/accounts/join')      
        else:
            user = User(
                username = username,
                password = PasswordHasher().hash(password1),
                start_period = start_period,
                end_period = end_period
            )
            user.save()
        return redirect('/')
    
        # joinform = JoinForm(request.POST)
        # if joinform.is_valid():
        #     user = User(
        #         username = username,
        #         password = PasswordHasher().hash(password1),
        #         start_period = start_period,
        #         end_period = end_period
        #     )
        #     user.save()
        #     return redirect('/')
    
        # else:
        #     context['forms']=joinform
        # return render(request, 'user/join.html',context)


# 로그인  
def login(request):
    loginform = LoginForm
    context ={ 'forms' : loginform }

    if request.method == 'GET':
        return render(request, 'Project/login.html', context)
    
    elif request.method == 'POST':
        loginform = LoginForm(request.POST)

        if loginform.is_valid():
            request.session['login_session'] = loginform.login_session
            request.session.set_expiry(0)
            return redirect('/')
        
        else:
            context['forms'] =loginform
            if loginform.errors:
                for value in loginform.errors.values():
                    context['error'] = value
        return render(request,'Project/login.html', context)

# 로그아웃   
def logout(request):
    request.session.flush()
    return redirect('/')