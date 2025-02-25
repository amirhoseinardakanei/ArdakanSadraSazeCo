from django.db import models

class Cooperate(models.Model):
    # مشخصات هویتی

    first_name = models.CharField(max_length=100, verbose_name="نام", blank=True, null=True, )
    last_name = models.CharField(max_length=100, verbose_name="نام خانوادگی", blank=True, null=True)
    name_changed = models.CharField(max_length=10, verbose_name="وضعیت تغیر نام", blank=True, null=True)
    previous_name = models.CharField(max_length=200, blank=True, null=True, verbose_name="نام و نام خانوادگی قبلی")
    gender = models.CharField(max_length=10, verbose_name="جنسیت", blank=True, null=True)
    photo = models.ImageField(upload_to='photos-user-cooperate/', verbose_name="عکس پرسنلی", blank=True, null=True)
    birth_date = models.CharField(max_length=10, verbose_name="تاریخ تولد", blank=True, null=True)
    father_name = models.CharField(max_length=100, verbose_name="نام پدر", blank=True, null=True)
    birth_number = models.CharField(max_length=10, verbose_name="شماره شناسنامه", blank=True, null=True)
    national_number = models.CharField(max_length=10, unique=True, verbose_name="شماره ملی", blank=True, null=True)
    birth_province = models.CharField(max_length=100, verbose_name="استان محل تولد", blank=True, null=True)
    birth_city = models.CharField(max_length=100, verbose_name="شهر محل تولد", blank=True, null=True)
    birth_cert_date = models.CharField(max_length=10, verbose_name="تاریخ صدور شناسنامه", blank=True, null=True)
    national_card_image = models.ImageField(upload_to='national_cards-user-cooperate/', verbose_name="تصویر کارت ملی", blank=True, null=True)
    national_card_back_image = models.ImageField(upload_to='national_cards-user-cooperate/', verbose_name="تصویر پشت کارت ملی", blank=True, null=True)
    birth_cert_image = models.ImageField(upload_to='birth_certs-user-cooperate/', verbose_name="تصویر شناسنامه", blank=True, null=True)
    birth_cert_page2_image = models.ImageField(upload_to='birth_certs-user-cooperate/', verbose_name="صفحه دوم شناسنامه", blank=True, null=True)
    birth_cert_page3_image = models.ImageField(upload_to='birth_certs-user-cooperate/', verbose_name="صفحه سوم شناسنامه", blank=True, null=True)
    birth_cert_page4_image = models.ImageField(upload_to='birth_certs-user-cooperate/', verbose_name="صفحه چهارم شناسنامه", blank=True, null=True)
    birth_cert_page5_image = models.ImageField(upload_to='birth_certs-user-cooperate/', verbose_name="صفحه پنجم شناسنامه", blank=True, null=True)
    step_1 = models.BooleanField(verbose_name='تکمیل مرحله اول', blank=True, null=True)

    # مشخصات خانوادگی و سکونت
    marital_status = models.CharField(max_length=10, verbose_name="وضعیت تاهل", blank=True, null=True)
    children_count = models.CharField(max_length=50, verbose_name="تعداد اولاد", blank=True, null=True)
    marriage_date = models.CharField(max_length=10, blank=True, null=True, verbose_name="تاریخ ازدواج")
    military_status = models.CharField(max_length=20, verbose_name="وضعیت نظام وظیفه", blank=True, null=True)
    exemption_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="نوع معافیت")
    military_service_start_date = models.CharField(max_length=10, blank=True, null=True, verbose_name="تاریخ شروع خدمت")
    military_service_end_date = models.CharField(max_length=10, blank=True, null=True, verbose_name="تاریخ پایان خدمت")
    military_card_image = models.ImageField(upload_to='military_cards/', blank=True, null=True, verbose_name="تصویر کارت پایان خدمت")
    residence_province = models.CharField(max_length=100, verbose_name="استان سکونت", blank=True, null=True)
    residence_city = models.CharField(max_length=100, verbose_name="شهر سکونت", blank=True, null=True)
    residence_address = models.TextField(verbose_name="آدرس محل سکونت", blank=True, null=True)
    residence_address_2 = models.TextField(verbose_name="آدرس دوم محل سکونت", blank=True, null=True)
    residence_work = models.TextField(verbose_name="آدرس محل کار", blank=True, null=True)
    residence_postcode = models.CharField(max_length=10, verbose_name="کد پستی محل سکونت", blank=True, null=True)
    phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن همراه", blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن اضطراری", blank=True, null=True)
    home_phone_number = models.CharField(max_length=11, verbose_name="شماره تلفن منزل", blank=True, null=True)
    email = models.EmailField(verbose_name="ایمیل", blank=True, null=True)
    step_2 = models.BooleanField(verbose_name='تکمیل مرحله دوم', blank=True, null=True)

    # مهارت و رزومه کاری
    desired_job_titles = models.TextField(verbose_name="عناوین شغل‌های درخواستی", blank=True, null=True)
    desired_job = models.CharField(max_length=100, verbose_name="عنوان شغل درخواستی", blank=True, null=True)
    education_level = models.CharField(max_length=50, verbose_name="مدرک تحصیلی", blank=True, null=True)
    field_of_study = models.CharField(max_length=100, blank=True, null=True, verbose_name="رشته تحصیلی")
    professional_certificates = models.TextField(blank=True, null=True, verbose_name="گواهینامه‌های فنی حرفه‌ای")
    skills = models.TextField(blank=True, null=True, verbose_name="مهارت‌ها")
    insurance_record_image = models.ImageField(upload_to='insurance_records/', blank=True, null=True, verbose_name="تصویر سابقه بیمه‌ای")
    driving_license_type = models.CharField(max_length=50, verbose_name="نوع گواهینامه رانندگی", blank=True, null=True)
    special_license_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="کد گواهینامه ویژه")
    driving_license_image = models.ImageField(upload_to='driving_licenses/', blank=True, null=True, verbose_name="تصویر گواهینامه")
    previous_work_experience = models.TextField(blank=True, null=True, verbose_name="سابقه کار قبلی")
    previous_company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام شرکت قبلی")
    previous_position = models.CharField(max_length=100, blank=True, null=True, verbose_name="سمت قبلی")
    previous_work_duration = models.CharField(max_length=100, blank=True, null=True, verbose_name="مدت زمان کار قبلی")
    previous_work_reference_image = models.ImageField(upload_to='work_references/', blank=True, null=True, verbose_name="تصویر رضایت‌نامه شرکت قبلی")
    referral_source = models.CharField(max_length=100, verbose_name="طریقه آشنایی با شرکت", blank=True, null=True)
    referral_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام معرف")
    referral_phone = models.CharField(max_length=11, blank=True, null=True, verbose_name="شماره تماس معرف")
    related_work_experience = models.TextField(blank=True, null=True, verbose_name="سابقه کار مرتبط با شرکت")
    employment_status = models.CharField(max_length=50, verbose_name="وضعیت اشتغال", blank=True, null=True)
    current_company_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام شرکت فعلی")
    current_position = models.CharField(max_length=100, blank=True, null=True, verbose_name="سمت فعلی")
    step_3 = models.BooleanField(verbose_name='تکمیل مرحله سوم', blank=True, null=True)

    # اطلاعات تکمیلی
    resume = models.FileField(upload_to='resumes/', verbose_name="رزومه", blank=True, null=True)
    mental_physical_status = models.TextField(verbose_name="وضعیت روحی و جسمانی", blank=True, null=True)
    requested_salary = models.CharField(max_length=100, verbose_name="حقوق درخواستی", blank=True, null=True)
    step_4 = models.BooleanField(verbose_name='تکمیل مرحله چهارم', blank=True, null=True)

    ok_no = models.BooleanField(verbose_name='تایید کاربر برای استخدام', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'درخواست استخدام'
        verbose_name_plural = 'درخواست های استخدام'