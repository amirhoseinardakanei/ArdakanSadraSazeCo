from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegistrationForm, LoginForm
from .models import User

# Create your views here.

class Register(View):
    def get(self, request):
        register_form = RegistrationForm()

        error_form = ''
        context = {
            'register_form': register_form,
            'error_form': error_form,
        }
        return render(request, 'PersonnelUserAccounts/Register.html', context)

    def post(self, request):
        register_form = RegistrationForm(request.POST)
        error_form = ''
        if register_form.is_valid():
            print(register_form.cleaned_data)
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            nationality = register_form.cleaned_data['national_number']
            phone_number = register_form.cleaned_data['phone_number']
            password = register_form.cleaned_data['password']

            user_nationality: bool = User.objects.filter(national_number__iexact=nationality).extra()
            user_phone_number: bool = User.objects.filter(phone_number__iexact=phone_number).extra()

            if user_nationality:
                register_form.add_error('national_number', 'این کد ملی قبلا توسط کاربر دیگری در سیستم ثبت شده است')
            elif user_phone_number:
                register_form.add_error('phone_number', 'این شماره تلفن قبلا توسط کاربر دیگری در سیستم ثبت شده است.')
            else:
                new_user = User(first_name=first_name, last_name=last_name, national_number=nationality, phone_number=phone_number, username=nationality)
                new_user.set_password(password)
                new_user.save()
                return render(request, 'PersonnelUserAccounts/StatusPage.html')

        else:
            error_form = ('تکمیل فرم شما با مشکل مواجه شده است. مشکل ها را اصلاح کنید!!!!!!!')

        context = {
            'register_form': register_form,
            'error_form': error_form,
        }
        return render(request, 'PersonnelUserAccounts/Register.html', context)
class Login(View):
    def get(self, request):
        login_form = LoginForm()


        context = {
            'login_form': login_form,
        }
        return render(request, 'PersonnelUserAccounts/Login.html', context)

    def post(self, request):
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            national_number = login_form.cleaned_data['national_number']
            password = login_form.cleaned_data['password']

            user: User = User.objects.filter(national_number=national_number).first()
            print(user)
            if user is not None:
                if user.check_password(password):
                    login(request, user)
                    if user.is_staff:
                        return redirect(reverse('admin:index'))
                    return redirect(reverse('UserPanelPage'))
                else:
                    login_form.add_error('national_number', 'کاربری با مشخیصات وارد شده پیدا نشد')
            else:
                login_form.add_error('national_number', 'کاربری با مشخیصات وارد شده پیدا نشد')

        context = {
            'login_form': login_form,
        }
        return render(request, 'PersonnelUserAccounts/Login.html', context)

class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('LoginPage'))


def SidebarComponent(request):
    status_user = bool(request.user.username)
    if status_user is False:
        return redirect(reverse('HomePage'))
    current_user = User.objects.filter(username=request.user.username).first()
    context = {
        'current_user': current_user,
    }

    return render(request, 'PersonnelUserAccounts/UserPanel/SidebarComponent.html', context)


class UserPanel(View):
    def get(self, request):
        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))
        current_user = User.objects.filter(username=request.user.username).first()
        context = {
            'current_user': current_user,
        }

        return render(request, 'PersonnelUserAccounts/UserPanel/IndexPanelPage.html', context)

