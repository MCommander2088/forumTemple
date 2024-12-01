from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

from forumTemple import settings


def index(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print("login data:", username, password)
        # 使用内置方法验证
        user = authenticate(username=username, password=password)

        # 验证通过
        if user:
            if not user.is_superuser:
                return render(request, 'admin_login.html', context={"result": "auth failed,you're not an admin!"})
            login(request, user)
            print("logged", user)
            return render(request, 'admin_index.html', context={"username": request.user.username})
        # 验证失败
        else:
            return render(request, 'admin_login.html', context={"result": "auth failed,password incorrect"})

    if request.method == "GET":
        if request.GET.get('act') == 'logout':
            print("logging out", request.user.username)
            logout(request)
            return render(request, 'admin_login.html', context={"result": "need login"})

        username = request.user.username
        if not username:
            return render(request, 'admin_login.html', context={"result": "need login"})

        print("got username:", request.user.username)
        return render(request, 'admin_index.html', context={"username": username})


def action(request):
    return JsonResponse({"statue": "success", "code": "200"})
