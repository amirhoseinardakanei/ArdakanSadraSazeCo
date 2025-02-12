from django.db import models


# Create your models here.

class SettingWeb(models.Model):
    banner = models.ImageField(upload_to='image-banner', verbose_name='تصویر بنر')
    banner4 = models.ImageField(upload_to='image-banner', verbose_name='تصویر بنر2', blank=True)
    banner3 = models.ImageField(upload_to='image-banner', verbose_name='تصویر بنر3', blank=True)
    aboutUS1 = models.TextField(verbose_name='متن درباره ما1')
    aboutUS2 = models.TextField(verbose_name='متن درباره ما2', blank=True)
    aboutUS3 = models.TextField(verbose_name='متن درباره ما3', blank=True)
    bannerUS1 = models.ImageField(upload_to='image-about-us', verbose_name='تصویر درباره ما1')
    bannerUS2 = models.ImageField(upload_to='image-about-us', verbose_name='تصویر درباره ما2')
    m1 = models.CharField(max_length=300, verbose_name='سابقه شرکت')
    m2 = models.CharField(max_length=300, verbose_name='تعداد پروژه های تکمیل شده')
    m3 = models.CharField(max_length=300, verbose_name='تعداد مشتری')
    m4 = models.CharField(max_length=300, verbose_name='تعداد اعضای پرسنل')
    banner2 = models.ImageField(upload_to='image-banner', verbose_name='تصویر بخش چرا شرکت صدرا سازه')
    ok_no = models.BooleanField(default=False, verbose_name='نمایش داده شود / نمایش داده نشود')

    def __str__(self):
        return 'تنظیمات'

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'


class ServiceWeb(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام خدمت')
    aboutUS2 = models.TextField(verbose_name='متن توضیح خدمات')
    slug = models.SlugField(verbose_name='عنوان در url')
    banner = models.ImageField(upload_to='image-service', verbose_name='تصویر خدمات', blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'خدمات '
        verbose_name_plural = 'خدمت ما'


class CeoSpeech(models.Model):

    speech1 = models.TextField(verbose_name='متن سخن مدیرعامل1')
    speech2 = models.TextField(verbose_name='متن سخن مدیرعامل2', blank=True)
    banner = models.ImageField(upload_to='image-ceo', verbose_name='تصویر مدیرعامل')



    def __str__(self):
        return ' سخن مدیر عامل'

    class Meta:
        verbose_name = ""
        verbose_name_plural = 'بخش سخن مدیرعامل'


class TeamCo(models.Model):
    name_pr = models.CharField(max_length=300, verbose_name='نام اعضای پرسنل')
    img_pr = models.ImageField(upload_to='image-team', verbose_name='تصویر پرسنل')



    def __str__(self):
        return self.name_pr

    class Meta:
        verbose_name = 'تیم ما'
        verbose_name_plural = 'پرسنل'


class LogoCompani(models.Model):
    name_co = models.CharField(max_length=300, verbose_name='نام شرکت کارفرما')
    img_co = models.ImageField(upload_to='logo-compani', verbose_name='لوگو شرکت کارفرما')



    def __str__(self):
        return self.name_co

    class Meta:
        verbose_name = 'لوگو'
        verbose_name_plural = 'ایجاد لوگو شرکت های کارفرما'



class TruckOne(models.Model):
    name = models.CharField(max_length=300, verbose_name='نوع مکانیزم')
    number = models.IntegerField( verbose_name='تعداد')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'تنظیمات ماشین آلات حمل'


class TruckTow(models.Model):
    name = models.CharField(max_length=300, verbose_name='نوع مکانیزم')
    number = models.IntegerField( verbose_name='تعداد')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'تنظیمات ماشین آلات راهسازی'


class TruckTree(models.Model):
    name = models.CharField(max_length=300, verbose_name='نوع مکانیزم')
    number = models.IntegerField( verbose_name='تعداد')



    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ماشین'
        verbose_name_plural = 'تنظیمات ماشین آلات بارگیری'