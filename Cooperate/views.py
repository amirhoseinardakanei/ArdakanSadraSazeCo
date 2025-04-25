from urllib import request
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic.base import TemplateView
from .forms import CooperationFormStep1, CooperationFormStep2, CooperationFormStep3, CooperationFormStep4
from .models import Cooperate
from PersonnelUserAccounts.models import User
import ast


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
        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)
            if cooperate_test_initial.step_1 == False:
                return redirect(reverse('CooperateStep_1'))
        else:
            return redirect(reverse('UserPanelPage'))

        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)

            if cooperate_test_initial.step_2 is True:
                form = CooperationFormStep2(
                    instance=cooperate_test_initial
                )
                marital_status = cooperate_test_initial.marital_status
                children_count = cooperate_test_initial.children_count
                birth_cert_date = cooperate_test_initial.marriage_date
                military_status = cooperate_test_initial.military_status
                exemption_type = cooperate_test_initial.exemption_type
                start_military_date = cooperate_test_initial.military_service_start_date
                end_military_date = cooperate_test_initial.military_service_end_date
                province = cooperate_test_initial.residence_province
                city = cooperate_test_initial.residence_city

                return render(request, 'Cooperate/CooperateStep_2.html', {
                    'form': form,
                    'marital_status': marital_status,
                    'children_count': children_count,
                    'birth_cert_date': birth_cert_date,
                    'military_status': military_status,
                    'exemption_type': exemption_type,
                    'start_military_date': start_military_date,
                    'end_military_date': end_military_date,
                    'province': province,
                    'city': city,
                    'status_step': bool(cooperate_test_initial.step_2),
            })

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
        exemption_type = '' if request.POST.get('exemption_type') == '' else request.POST.get('exemption_type')
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
            children_count = ''
            birth_cert_date = '0000-00-00'
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

                return redirect(reverse('CooperateStep_3'))



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

        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)
            if cooperate_test_initial.step_2 == False:
                return redirect(reverse('CooperateStep_2'))
        else:
            return redirect(reverse('UserPanelPage'))

        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)

            if cooperate_test_initial.step_3 is True:
                form = CooperationFormStep3(
                    instance=cooperate_test_initial
                )

                topicses = cooperate_test_initial.desired_job_titles
                degree = cooperate_test_initial.education_level
                fieldـstudy = cooperate_test_initial.field_of_study
                picture_insurance_history = cooperate_test_initial.insurance_record_image
                type_driver_license = cooperate_test_initial.driving_license_type
                codep = cooperate_test_initial.special_license_code
                acknowledgment_image = cooperate_test_initial.driving_license_image
                work_history = cooperate_test_initial.previous_work_experience
                name_company = cooperate_test_initial.previous_company_name
                semat_work = cooperate_test_initial.previous_position
                time_work_history = cooperate_test_initial.previous_work_duration
                img_certificate_work = cooperate_test_initial.previous_work_reference_image
                know_our_company = cooperate_test_initial.referral_source
                representative_name = cooperate_test_initial.referral_name
                representative_phone_number = cooperate_test_initial.referral_phone
                relatedـworkـexperience = cooperate_test_initial.relatedـworkـexperience
                descriptionـrelatedـwork = cooperate_test_initial.descriptionـrelatedـwork
                employmentـstatus = cooperate_test_initial.employment_status
                online_company = cooperate_test_initial.current_company_name
                semat_online_company = cooperate_test_initial.current_position

                return render(request, 'Cooperate/CooperateStep_3.html', {
                    'form': form,
                    'topicses': ast.literal_eval(topicses),
                    'degree': degree,
                    'fieldـstudy': fieldـstudy,
                    'picture_insurance_history': picture_insurance_history,
                    'type_driver_license': type_driver_license,
                    'codep': codep,
                    'acknowledgment_image': acknowledgment_image,
                    'work_history': work_history,
                    'name_company': name_company,
                    'semat_work': semat_work,
                    'time_work_history': time_work_history,
                    'img_certificate_work': img_certificate_work,
                    'know_our_company': know_our_company,
                    'representative_name': representative_name,
                    'representative_phone_number': representative_phone_number,
                    'relatedـworkـexperience': relatedـworkـexperience,
                    'descriptionـrelatedـwork': descriptionـrelatedـwork,
                    'employmentـstatus': employmentـstatus,
                    'online_company': online_company,
                    'semat_online_company': semat_online_company,
                    'status_step': bool(cooperate_test_initial.step_3),
                })

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
        fieldـstudy = '' if request.POST.get('fieldـstudy') == '' else request.POST.get('fieldـstudy') # رشته تحصیلی
        fieldـstudy_status = False
        if degree != '0':
            if degree == 'سیکل':
                 fieldـstudy_status = True
            else:
                if fieldـstudy != '':
                    fieldـstudy_status = True
                else:
                    fieldـstudy_status = False
        # هندل کردن داینامیک فیلد مدرک تحصیلی

        picture_insurance_history = '0' if request.FILES.get('picture_insurance_history') == None else request.FILES.get('picture_insurance_history')

        # هندل کردن داینامیک فیلد گواهینامه
        type_driver_license = '0' if request.POST.get('type_driver_license') == '0' else request.POST.get('type_driver_license')  # نوع گواهینامه رانندگی
        codep = '' if request.POST.get('codep') == '' else request.POST.get('codep')  # کد ویژه
        codep_status = False
        if type_driver_license != '0':
            if type_driver_license == 'کد ویژه':
                if codep != '':
                    codep_status = True
                else:
                    codep_status = False
            else:
                codep_status = True
        acknowledgment_image = '0' if request.FILES.get('acknowledgment_image') == None else request.FILES.get('acknowledgment_image') # تصویر گواهینامه
        # هندل کردن داینامیک فیلد گواهینامه


        # هندل کردن داینامیک فیلد قبلا با مجموعه ای کار داشتین
        work_history = '0' if request.POST.get('work_history') == '0' else request.POST.get('work_history') # وضعیت کار با مجموعه ی دیگر
        work_history_status = False

        name_company = '' if request.POST.get('name_company') == None else request.POST.get('name_company') # نام شرکت قبلی
        semat_work = '' if request.POST.get('semat_work') == None else request.POST.get('semat_work') # سمت کاربر در شرکت قبلی
        time_work_history = '' if request.POST.get('time_work_history') == None else request.POST.get('time_work_history') # مدت زمان کار با شرکت قبلی
        img_certificate_work = '0' if request.FILES.get('img_certificate_work') == None else request.FILES.get('img_certificate_work') # تصویر رضایت نامه از شرکت قبلی

        if work_history != '0':
            if work_history == 'بله':
                if name_company != '' and semat_work != '' and time_work_history != '' and img_certificate_work != '0':
                    work_history_status = True
                else:
                    work_history_status = False
            else:
                work_history_status = True
        # هندل کردن داینامیک فیلد قبلا با مجموعه ای کار داشتین

        # هندل کردن داینامیک فیلد طریقه آشنایی با شرکت ما
        know_our_company = '0' if request.POST.get('know_our_company') == '0' else request.POST.get('know_our_company') # نحوه آشنایی با شرکت ما
        know_our_company_status = False
        representative_name = '' if request.POST.get('representative_name') == '' else request.POST.get('representative_name') # نام معرف
        representative_phone_number = '' if request.POST.get('representative_phone_number') == '' else request.POST.get('representative_phone_number') # شماره تلفن معرف
        if know_our_company != '0':
            if know_our_company == 'معرف':
                if representative_name != '' and representative_phone_number != '':
                    know_our_company_status = True
                else:
                    know_our_company_status = False
            else:
                know_our_company_status = True
        # هندل کردن داینامیک فیلد طریقه آشنایی با شرکت ما

        # هندل کردن داینامیک فیلد داری سابقه کاری با حوزه مرتبط با صدرا سازه هستم
        relatedـworkـexperience = '0' if request.POST.get('relatedـworkـexperience') == '0' else request.POST.get('relatedـworkـexperience') # وضعیت سابقه کاریی با حوره مرتبط با صدرا سازه
        relatedـworkـexperience_status = False
        descriptionـrelatedـwork = '' if request.POST.get('descriptionـrelatedـwork') == '' else request.POST.get('descriptionـrelatedـwork') # توضیح درباره حوزه کاری مرتبط
        if relatedـworkـexperience != '0':
            if relatedـworkـexperience == 'بله':
                if descriptionـrelatedـwork != '':
                    relatedـworkـexperience_status = True
                else:
                    relatedـworkـexperience_status = False
            else:
                relatedـworkـexperience_status = True
        # هندل کردن داینامیک فیلد داری سابقه کاری با حوزه مرتبط با صدرا سازه هستم

        # هندل کردن داینامیک فیلد وضعیت اشتغال
        employmentـstatus = '0' if request.POST.get('employmentـstatus') == '0' else request.POST.get('employmentـstatus')
        employmentـstatus_status = False
        online_company = '' if request.POST.get('online_company') == '' else request.POST.get('online_company')
        semat_online_company = '' if request.POST.get('semat_online_company') == '' else request.POST.get('semat_online_company')
        if employmentـstatus != '0':
            if employmentـstatus == 'شاغل':
                if online_company != '' and semat_online_company != '':
                    employmentـstatus_status = True
                else:
                    employmentـstatus_status = False
            else:
                employmentـstatus_status = True
        # هندل کردن داینامیک فیلد وضعیت اشتغال

        if topicses != '0' and degree != '0' and fieldـstudy_status == True and picture_insurance_history != '0' and type_driver_license != '0' and codep_status == True and acknowledgment_image != '0' and work_history != '0' and work_history_status == True and know_our_company != '0' and know_our_company_status == True and relatedـworkـexperience != '0' and relatedـworkـexperience_status == True and employmentـstatus != '0' and employmentـstatus_status == True:
            if form.is_valid():
                form.save()
                cooperate = Cooperate.objects.get(national_number=request.user.national_number)

                cooperate.desired_job_titles = topicses
                cooperate.education_level = degree
                cooperate.field_of_study = fieldـstudy
                cooperate.insurance_record_image = picture_insurance_history
                cooperate.driving_license_type = type_driver_license
                cooperate.special_license_code = codep
                cooperate.driving_license_image = acknowledgment_image
                cooperate.previous_work_experience = work_history
                cooperate.previous_company_name = name_company
                cooperate.previous_position = semat_work
                cooperate.previous_work_duration = time_work_history
                cooperate.previous_work_reference_image = img_certificate_work
                cooperate.referral_source = know_our_company
                cooperate.referral_name = representative_name
                cooperate.referral_phone = representative_phone_number
                cooperate.related_work_experience = relatedـworkـexperience
                cooperate.descriptionـrelatedـwork = descriptionـrelatedـwork
                cooperate.employment_status = employmentـstatus
                cooperate.current_company_name = online_company
                cooperate.current_position = semat_online_company
                cooperate.step_3 = True
                cooperate.save()
                return redirect(reverse('CooperateStep_4'))





        context_post = {
            'form': form,
            'topicses': topicses,
            'degree': degree,
            'fieldـstudy': fieldـstudy,
            'picture_insurance_history': picture_insurance_history,
            'type_driver_license': type_driver_license,
            'codep': codep,
            'acknowledgment_image': acknowledgment_image,
            'work_history': work_history,
            'name_company': name_company,
            'semat_work': semat_work,
            'time_work_history': time_work_history,
            'img_certificate_work': img_certificate_work,
            'know_our_company' : know_our_company,
            'representative_name': representative_name,
            'representative_phone_number': representative_phone_number,
            'relatedـworkـexperience': relatedـworkـexperience,
            'descriptionـrelatedـwork': descriptionـrelatedـwork,
            'employmentـstatus': employmentـstatus,
            'online_company': online_company,
            'semat_online_company': semat_online_company,
        }

        return render(request, 'Cooperate/CooperateStep_3.html', context_post)

class CooperateStep_4(View):
    def get(self, request):
        status_user = bool(request.user.username)
        if status_user is False:
            return redirect(reverse('HomePage'))

        if Cooperate.objects.filter(national_number=request.user.national_number).exists():
            cooperate_test_initial = Cooperate.objects.get(national_number=request.user.national_number)
            if cooperate_test_initial.step_3 == False:
                return redirect(reverse('CooperateStep_3'))
        else:
            return redirect(reverse('UserPanelPage'))

        form = CooperationFormStep4()
        context_get = {
            'form': form,
        }
        return render(request, 'Cooperate/CooperateStep_4.html', context_get)

    def post(self, request):
        cooperate_instance = Cooperate.objects.get(national_number=request.user.national_number)

        form = CooperationFormStep4(request.POST, instance=cooperate_instance)

        img_certificate = '0' if request.FILES.get('certificate') == None else request.FILES.get('certificate')

        if img_certificate != '0':
            if form.is_valid():
                form.save()
                cooperate = Cooperate.objects.get(national_number=request.user.national_number)
                cooperate.resume = img_certificate
                cooperate.step_4 = True
                cooperate.save()
                return redirect(reverse('UserPanelPage'))

        context_post = {
            'form': form,
            'img_certificate': img_certificate,
        }

        return render(request, 'Cooperate/CooperateStep_4.html', context_post)