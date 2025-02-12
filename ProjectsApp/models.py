from django.db import models

# Create your models here.


class ProjectsOpen(models.Model):
    name = models.CharField(max_length=300, verbose_name='عنوان پروژه')
    ceo = models.CharField(max_length=300, verbose_name='کارفرما پروژه')
    calendar = models.CharField(max_length=300, verbose_name='تاریخ شروع پروژه')
    category = models.CharField(max_length=300, verbose_name='دسته بندی پروژه')
    img_1 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 1')
    img_2 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 2', blank=True)
    img_3 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 3', blank=True)
    img_4 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 4', blank=True)
    img_5 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 5', blank=True)
    description_1 = models.TextField(verbose_name='بند 1 توضیحات پروژه')
    description_2 = models.TextField(verbose_name='بند 2 توضیحات پروژه', blank=True)
    description_3 = models.TextField(verbose_name='بند 3 توضیحات پروژه', blank=True)
    slug = models.SlugField(verbose_name='عنوان در url', null=True)
    boolean = models.BooleanField(default=False, null=True, verbose_name='در صفحه اصلی نمایش داده شود / نشود')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پروژه '
        verbose_name_plural = 'پروژه های درحال اجرا'


class ProjectsOpenMine(models.Model):
    name = models.CharField(max_length=300, verbose_name='عنوان پروژه')
    ceo = models.CharField(max_length=300, verbose_name='مالکیت پروژه')
    calendar = models.CharField(max_length=300, verbose_name='تاریخ شروع پروژه')
    category = models.CharField(max_length=300, verbose_name='دسته بندی پروژه')
    img_1 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 1')
    img_2 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 2', blank=True)
    img_3 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 3', blank=True)
    img_4 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 4', blank=True)
    img_5 = models.ImageField(upload_to='img-project-open', verbose_name='تصویر پروژه 5', blank=True)
    description_1 = models.TextField(verbose_name='بند 1 توضیحات پروژه')
    description_2 = models.TextField(verbose_name='بند 2 توضیحات پروژه', blank=True)
    description_3 = models.TextField(verbose_name='بند 3 توضیحات پروژه', blank=True)
    slug = models.SlugField(verbose_name='عنوان در url', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه های معدنی درحال اجرا'


class ProjectsClosed(models.Model):
    name = models.CharField(max_length=300, verbose_name='عنوان پروژه')
    ceo = models.CharField(max_length=300, verbose_name='کارفرما پروژه')
    calendar = models.CharField(max_length=300, verbose_name='تاریخ شروع پروژه', blank=True)
    category = models.CharField(max_length=300, verbose_name='شماره قرارداد', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پروژه '
        verbose_name_plural = 'پروژه های به پایان رسیده'