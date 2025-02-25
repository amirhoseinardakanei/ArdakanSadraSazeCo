from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CooperationFormStep1, CooperationFormStep2, CooperationFormStep3
from .models import Cooperate
from PersonnelUserAccounts.models import User


# Create your views here.
def Redirect_Step(request):
    if Cooperate.objects.filter(national_number=request.user.national_number).exists():
        cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)
        if cooperate_test_initial.step_4:
            return redirect(reverse('UserPanelPage'))

        if cooperate_test_initial.step_3:
            return redirect(reverse('CooperateStep_4'))

        if cooperate_test_initial.step_2:
            return redirect(reverse('CooperateStep_3'))

        if cooperate_test_initial.step_1:
            return redirect(reverse('CooperateStep_2'))
    else:
        return redirect(reverse('CooperateStep_1'))

class CooperateStep_1(View):

    def get(self, request):
        status_user = bool(request.user.national_number)
        if status_user is False:
            return redirect(reverse('HomePage'))


        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)

            if cooperate_test_initial.step_1 is True:
                form = CooperationFormStep1(
                    instance=cooperate_test_initial
                )
                name_change = cooperate_test_initial.name_changed
                previous_name = cooperate_test_initial.previous_name
                gender = cooperate_test_initial.gender
                birth_province = cooperate_test_initial.birth_province
                birth_city = cooperate_test_initial.birth_city
                print(previous_name)
                return render(request, 'Cooperate/CooperateStep_1.html', {
                    'form': form,
                    'name_change': name_change,
                    'previous_name': previous_name,
                    'gender_intial': gender,
                    'birth_province': birth_province,
                    'birth_city': birth_city,
                    'status_step': bool(cooperate_test_initial.step_1),
            })

        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))
        current_user = User.objects.filter(national_number=request.user.national_number).first()


        form = CooperationFormStep1()


        context_get = {
            'form': form,
        }



        return render(request, 'Cooperate/CooperateStep_1.html', context_get)


    def post(self, request):
        # چک کردن برای اینکه یوزر لاگین هست سا خیر
        status_user = bool(request.user.national_number)
        if status_user is False:
            return redirect(reverse('HomePage'))
        # چک کردن برای اینکه یوزر لاگین هست سا خیر

        # فرم تغیر دیتا برای مرحله اول
        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)

            if cooperate_test_initial.step_1 is True:
                form_initial = CooperationFormStep1(request.POST, instance=cooperate_test_initial)

                province = request.POST.get('province')
                city = request.POST.get('city')
                check_img = '0' if request.FILES.get('img3/4') == None else request.FILES.get('img3/4')
                img_card_national = '0' if request.FILES.get('img-card-national') == None else request.FILES.get(
                    'img-card-national')
                img_card_national2 = '0' if request.FILES.get('img-card-national2') == None else request.FILES.get(
                    'img-card-national2')
                img_card_certificate = '0' if request.FILES.get('img-card-certificate') == None else request.FILES.get(
                    'img-card-certificate')
                gender = request.POST.get('gender')
                name_change = request.POST.get('name_change')
                name_previous = '0' if request.POST.get('name_previous') == '' else request.POST.get('name_previous')

                if check_img != '0' and img_card_national != '0' and img_card_national2 != '0' and img_card_certificate != '0' and province != '0' and city != '0' and gender != '0' and name_change != '0':
                    if name_change == 'بله':
                        if name_previous != '0':

                            current_user = User.objects.filter(national_number=request.user.national_number).first()

                            if form_initial.is_valid():

                                if form_initial.cleaned_data['national_number'] == str(current_user):

                                    form_initial.save()
                                    cooperate = Cooperate.objects.get(
                                        national_number=form_initial.cleaned_data['national_number'])

                                    # اختصاص فایل‌ها و داده‌ها به شیء
                                    cooperate.name_changed = name_change
                                    cooperate.previous_name = name_previous
                                    cooperate.gender = gender
                                    cooperate.photo = request.FILES.get('img3/4')
                                    cooperate.birth_province = request.POST.get('province')
                                    cooperate.birth_city = request.POST.get('city')
                                    cooperate.national_card_image = request.FILES.get('img-card-national')
                                    cooperate.national_card_back_image = request.FILES.get('img-card-national2')
                                    cooperate.birth_cert_image = request.FILES.get('img-card-certificate')
                                    cooperate.birth_cert_page2_image = request.FILES.get('img-card-certificate2')
                                    cooperate.birth_cert_page3_image = request.FILES.get('img-card-certificate3')
                                    cooperate.birth_cert_page4_image = request.FILES.get('img-card-certificate4')
                                    cooperate.birth_cert_page5_image = request.FILES.get('img-card-certificate5')
                                    cooperate.step_1 = True
                                    cooperate.save()
                                    return redirect(reverse('CooperateStep_2'))
                                else:
                                    form.add_error('national_number', 'این کد ملی با کد ملی شما مغایرت دارد.')
                    else:
                        current_user = User.objects.filter(national_number=request.user.national_number).first()

                        if form_initial.is_valid():

                            if form_initial.cleaned_data['national_number'] == str(current_user):

                                form_initial.save()
                                cooperate = Cooperate.objects.get(national_number=form_initial.cleaned_data['national_number'])

                                # اختصاص فایل‌ها و داده‌ها به شیء
                                cooperate.name_changed = name_change
                                cooperate.previous_name = name_previous
                                cooperate.gender = gender
                                cooperate.photo = request.FILES.get('img3/4')
                                cooperate.birth_province = request.POST.get('province')
                                cooperate.birth_city = request.POST.get('city')
                                cooperate.national_card_image = request.FILES.get('img-card-national')
                                cooperate.national_card_back_image = request.FILES.get('img-card-national2')
                                cooperate.birth_cert_image = request.FILES.get('img-card-certificate')
                                cooperate.birth_cert_page2_image = request.FILES.get('img-card-certificate2')
                                cooperate.birth_cert_page3_image = request.FILES.get('img-card-certificate3')
                                cooperate.birth_cert_page4_image = request.FILES.get('img-card-certificate4')
                                cooperate.birth_cert_page5_image = request.FILES.get('img-card-certificate5')
                                cooperate.step_1 = True
                                cooperate.save()
                                return redirect(reverse('CooperateStep_2'))
                            else:
                                form.add_error('national_number', 'این کد ملی با کد ملی شما مغایرت دارد.')
        # فرم تغیر دیتا برای مرحله اول


        # واکشی دیتا برای چک کردن
        form = CooperationFormStep1(request.POST, request.FILES)
        province = request.POST.get('province')
        city = request.POST.get('city')
        check_img = '0' if request.FILES.get('img3/4') == None else request.FILES.get('img3/4')
        img_card_national = '0' if request.FILES.get('img-card-national') == None else request.FILES.get('img-card-national')
        img_card_national2 = '0' if request.FILES.get('img-card-national2') == None else request.FILES.get('img-card-national2')
        img_card_certificate = '0' if request.FILES.get('img-card-certificate') == None else request.FILES.get('img-card-certificate')
        gender = request.POST.get('gender')
        name_change = request.POST.get('name_change')
        name_previous = '0' if request.POST.get('name_previous') == '' else request.POST.get('name_previous')
        # واکشی دیتا برای چک کردن

        # چک کردن دیتا برای زخیره مرحله اول
        if check_img != '0' and img_card_national != '0' and img_card_national2 != '0' and img_card_certificate != '0' and province != '0' and city != '0' and gender != '0' and name_change != '0':
            if name_change == 'بله':
                if name_previous != '0':

                    current_user = User.objects.filter(national_number=request.user.national_number).first()

                    if form.is_valid():

                        if form.cleaned_data['national_number'] == str(current_user):

                            form.save()
                            cooperate = Cooperate.objects.get(national_number=form.cleaned_data['national_number'])

                            # اختصاص فایل‌ها و داده‌ها به شیء
                            cooperate.name_changed = name_change
                            cooperate.previous_name = name_previous
                            cooperate.gender = gender
                            cooperate.photo = request.FILES.get('img3/4')
                            cooperate.birth_province = request.POST.get('province')
                            cooperate.birth_city = request.POST.get('city')
                            cooperate.national_card_image = request.FILES.get('img-card-national')
                            cooperate.national_card_back_image = request.FILES.get('img-card-national2')
                            cooperate.birth_cert_image = request.FILES.get('img-card-certificate')
                            cooperate.birth_cert_page2_image = request.FILES.get('img-card-certificate2')
                            cooperate.birth_cert_page3_image = request.FILES.get('img-card-certificate3')
                            cooperate.birth_cert_page4_image = request.FILES.get('img-card-certificate4')
                            cooperate.birth_cert_page5_image = request.FILES.get('img-card-certificate5')
                            cooperate.step_1 = True
                            cooperate.save()
                            return redirect(reverse('CooperateStep_2'))
                        else:
                            form.add_error('national_number', 'این کد ملی با کد ملی شما مغایرت دارد.')
            else:
                current_user = User.objects.filter(national_number=request.user.national_number).first()

                if form.is_valid():

                    if form.cleaned_data['national_number'] == str(current_user):

                        form.save()
                        cooperate = Cooperate.objects.get(national_number=form.cleaned_data['national_number'])

                        # اختصاص فایل‌ها و داده‌ها به شیء
                        cooperate.name_changed = name_change
                        cooperate.previous_name = name_previous
                        cooperate.gender = gender
                        cooperate.photo = request.FILES.get('img3/4')
                        cooperate.birth_province = request.POST.get('province')
                        cooperate.birth_city = request.POST.get('city')
                        cooperate.national_card_image = request.FILES.get('img-card-national')
                        cooperate.national_card_back_image = request.FILES.get('img-card-national2')
                        cooperate.birth_cert_image = request.FILES.get('img-card-certificate')
                        cooperate.birth_cert_page2_image = request.FILES.get('img-card-certificate2')
                        cooperate.birth_cert_page3_image = request.FILES.get('img-card-certificate3')
                        cooperate.birth_cert_page4_image = request.FILES.get('img-card-certificate4')
                        cooperate.birth_cert_page5_image = request.FILES.get('img-card-certificate5')
                        cooperate.step_1 = True
                        cooperate.save()
                        return redirect(reverse('CooperateStep_2'))
                    else:
                        form.add_error('national_number', 'این کد ملی با کد ملی شما مغایرت دارد.')
        # چک کردن دیتا برای زخیره مرحله اول

        context_post = {
            'form': form,
            'check_img': check_img,
            'province': province,
            'city': city,
            'img_card_national': img_card_national,
            'img_card_national2': img_card_national2,
            'img_card_certificate': img_card_certificate,
            'gender' : gender,
            'name_change' : name_change,
            'name_previous' : name_previous,
        }


        return render(request, 'Cooperate/CooperateStep_1.html', context_post)


class CooperateStep_2(View):
    def get(self, request):
        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))

        form = CooperationFormStep2()

        context_get = {
            'form': form,
        }

        return render(request, 'Cooperate/CooperateStep_2.html', context_get)

    def post(self, request):
        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))

        cooperate_instance = Cooperate.objects.get(national_number=request.user.national_number)
        form = CooperationFormStep2(request.POST, instance=cooperate_instance)

        marital_status = '0' if request.POST.get('marital_status') == None else request.POST.get('marital_status')
        children_count = '0' if request.POST.get('children_count') == None else request.POST.get('children_count')
        birth_cert_date = '0000-00-00' if request.POST.get('birth_cert_date') == '' else request.POST.get('birth_cert_date')
        military_status = '0' if request.POST.get('military_status') == None else request.POST.get('military_status')
        exemption_type = '0' if request.POST.get('exemption_type') == '' else request.POST.get('exemption_type')
        img_card_military = '0' if request.FILES.get('img_card_military') == None else request.FILES.get('img_card_military')
        start_military_date = '0000-00-00' if request.POST.get('start_military_date') == '' else request.POST.get('start_military_date')
        end_military_date = '0000-00-00' if request.POST.get('end_military_date') == '' else request.POST.get('end_military_date')
        province = request.POST.get('province')
        city = request.POST.get('city')
        marital = False
        military = False

        if marital_status == 'متاهل':
            if children_count != '0' and birth_cert_date != '0':
                marital = True
            else:
                marital = False
        elif marital_status == 'مجرد':
            marital = True

        if military_status == 'معافیت':
            if exemption_type != '0':
                military = True
            else:
                military = False
        elif military_status == 'پایان خدمت':
            if img_card_military != '0' and start_military_date != '0' and end_military_date != '0':
                military = True
            else:
                military = False

        if marital_status != '0' and military_status != '0' and marital == True and province != "0" and city != "0" and marital == True and military == True:
            if form.is_valid():
                cooperate_instance = Cooperate.objects.get(national_number=request.user.national_number)


                form.save()

                cooperate = Cooperate.objects.get(national_number=request.user.national_number)

                cooperate.marital_status = marital_status
                cooperate.children_count = children_count
                cooperate.marriage_date = birth_cert_date
                cooperate.military_status = military_status
                cooperate.exemption_type = exemption_type
                cooperate.military_card_image = img_card_military
                cooperate.military_service_start_date = start_military_date
                cooperate.military_service_end_date = end_military_date
                cooperate.residence_province = province
                cooperate.residence_city = city
                cooperate.step_2 = True
                cooperate.save()

                return redirect(reverse('HomePage'))



        context_post = {
            'form': form,
            'marital_status': marital_status,
            'children_count': children_count,
            'birth_cert_date': birth_cert_date,
            'military_status': military_status,
            'exemption_type': exemption_type,
            'img_card_military': img_card_military,
            'start_military_date': start_military_date,
            'end_military_date': end_military_date,
            'province': province,
            'city': city,

        }

        return render(request, 'Cooperate/CooperateStep_2.html', context_post)


class CooperateStep_3(View):
    def get(self, request):
        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))

        form = CooperationFormStep3()

        context_get = {
            'form': form,
        }

        return render(request, 'Cooperate/CooperateStep_3.html', context_get)

    def post(self, request):
        cooperate_instance = Cooperate.objects.get(national_number=request.user.national_number)

        form = CooperationFormStep3(request.POST, instance=cooperate_instance)

       # هندل کردن شغل های درخواستی
        topicses = '0' if request.POST.getlist('topics') == [] else request.POST.getlist('topics') # لیست شغل های درخواستی
        txt_topics = """"""
        for topic in topicses:
            txt_topics = f'{txt_topics} | {topic}'
        # هندل کردن شغل های درخواستی

        # هندل کردن داینامیک فیلد مدرک تحصیلی
        degree = '0' if request.POST.get('degree') == '0' else request.POST.get('degree') # مدرک تحصیلی
        fieldـstudy = '0' if request.POST.get('fieldـstudy') == '' else request.POST.get('fieldـstudy') # رشته تحصیلی
        fieldـstudy_status = False
        if degree != '0':
            if degree == 'سیکل':
                 fieldـstudy_status = True
            else:
                if fieldـstudy != '0':
                    fieldـstudy_status = True
                else:
                    fieldـstudy_status = False
        # هندل کردن داینامیک فیلد مدرک تحصیلی




        context_post = {
            'form': form,
        }

        return render(request, 'Cooperate/CooperateStep_3.html', context_post)