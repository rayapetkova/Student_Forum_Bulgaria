from django.shortcuts import render


def register_user(request):
    return render(request, 'accounts/register_page.html')


def login_user(request):
    return render(request, 'accounts/login_page.html')
