from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
import re

class RegistrationForm(forms.Form):
    first_name = forms.CharField(
        label='نام',
        max_length=50,  # محدودیت تعداد کاراکتر
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام',
        }),
        validators=[
            validators.RegexValidator(
                regex=r'^[آ-ی\s]+$',
                message='نام فقط باید شامل حروف فارسی باشد.'
            )
        ]
    )
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        # بررسی اینکه فقط حروف فارسی و فاصله مجاز باشند
        if not re.match(r'^[آ-ی\s]+$', first_name):
            raise ValidationError('نام فقط باید شامل حروف فارسی باشد و اعداد یا کاراکترهای خاص مجاز نیستند.')

        return first_name

    last_name = forms.CharField(
        label='نام خاوادگی',
        max_length=50,  # محدودیت تعداد کاراکتر
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام خانوادگی (کامل و با پسوند)',
        }),
        validators=[
            validators.RegexValidator(
                regex=r'^[آ-ی\s]+$',
                message='نام خانوادگی  فقط باید شامل حروف فارسی باشد.'
            )
        ]
    )
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        # بررسی اینکه فقط حروف فارسی و فاصله مجاز باشند
        if not re.match(r'^[آ-ی\s]+$', last_name):
            raise ValidationError('نام خانوادگی فقط باید شامل حروف فارسی باشد و اعداد یا کاراکترهای خاص مجاز نیستند.')

        return last_name

    national_number = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد ملی',
        }),
        validators=[
            validators.RegexValidator(
                regex=r'^\d{10}$',
                message='کد ملی باید دقیقاً ۱۰ رقم عددی باشد.'
            )
        ]
    )

    phone_number = forms.CharField(
        label='شماره تلفن',
        max_length=11,  # شماره تلفن باید دقیقاً ۱۱ رقم باشد
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'شماره تلفن',
        }),
        validators=[
            validators.RegexValidator(
                regex=r'^09\d{9}$',
                message="شماره تلفن باید با 09 شروع شده و 11 رقم باشد."
            )
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        }),
        min_length=8,  # حداقل ۸ کاراکتر
        error_messages={
            'min_length': 'رمز عبور باید حداقل ۸ کاراکتر باشد.'
        }
    )
    def clean_password(self):
        password = self.cleaned_data.get('password')

        # جلوگیری از استفاده از 12345678 و ترکیبات مشابه
        weak_patterns = [r'12345678', r'87654321', r'11111111']
        for pattern in weak_patterns:
            if re.search(pattern, password):
                raise ValidationError('رمز عبور نباید شامل یک رمز ساده مانند "12345678" باشد.')

        return password

    password_repeat = forms.CharField(
        label='رمز رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور',
        })
    )
    def clean_password_repeat(self):

        password = self.cleaned_data.get('password')
        password_repeat = self.cleaned_data.get('password_repeat')

        if password and password_repeat and password != password_repeat:
            self.add_error('password_repeat', 'رمز‌های عبور مطابقت ندارند.')

        return self.cleaned_data


class LoginForm(forms.Form):
    national_number = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'کد ملی',
        }),
        validators=[
            validators.RegexValidator(
                regex=r'^\d{10}$',
                message='کد ملی باید دقیقاً ۱۰ رقم عددی باشد.'
            )
        ]
    )

    password = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',
        }),

        error_messages={
            'min_length': 'رمز عبور باید حداقل ۸ کاراکتر باشد.'
        }
    )
