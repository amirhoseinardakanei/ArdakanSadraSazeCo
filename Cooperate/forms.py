from django import forms
from .models import Cooperate

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator


class CooperationFormStep1(forms.ModelForm):
    class Meta:
        model = Cooperate
        fields = [
            'first_name',
            'last_name',
            'father_name',
            'birth_number',
            'national_number',
            'birth_date',
            'birth_cert_date',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی (با پیشوند یا پسوند)'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام پدر'}),
            'birth_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره شناسنامه', 'maxlength': '10'}),
            'national_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره ملی', 'maxlength': '10'}),
            'birth_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تاریخ تولد','autocomplete': 'off', 'data-jdp': '', 'onkeydown': 'return false', 'onclick': 'this.removeAttribute("readonly")'}),
            'birth_cert_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'تاریخ صدور شناسنامه','autocomplete': 'off', 'data-jdp': '', 'onkeydown': 'return false', 'onclick': 'this.removeAttribute("readonly")'}),
        }


    # اعتبارسنجی سفارشی برای فیلدها
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name:
            raise forms.ValidationError("این فیلد اجباری است.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name:
            raise forms.ValidationError("این فیلد اجباری است.")
        return last_name

    def clean_previous_name(self):
        previous_name = self.cleaned_data.get('previous_name')
        if not previous_name:
            raise forms.ValidationError("این فیلد اجباری است.")

    def clean_father_name(self):
        father_name = self.cleaned_data.get('father_name')
        if not father_name:
            raise forms.ValidationError("این فیلد اجباری است.")
        return father_name

    def clean_birth_number(self):
        birth_number = self.cleaned_data.get('birth_number')
        if not birth_number:
            raise forms.ValidationError("این فیلد اجباری است.")
        return birth_number

    def clean_national_number(self):
        national_number = self.cleaned_data.get('national_number')
        if not national_number:
            raise forms.ValidationError("این فیلد اجباری است.")
        if len(national_number) != 10:
            raise forms.ValidationError("شماره ملی باید ۱۰ رقم باشد.")
        return national_number

    def clean_birth_date(self):
        birth_date = self.cleaned_data.get('birth_date')
        if not birth_date:
            raise forms.ValidationError("این فیلد اجباری است.")
        return birth_date

    def clean_birth_cert_date(self):
        birth_cert_date = self.cleaned_data.get('birth_cert_date')
        if not birth_cert_date:
            raise forms.ValidationError("این فیلد اجباری است.")
        return birth_cert_date


class CooperationFormStep2(forms.ModelForm):

    class Meta:
        model = Cooperate
        fields = [
            'residence_address',
            'residence_address_2',
            'residence_work',
            'residence_postcode',
            'phone_number',
            'emergency_phone_number',
            'home_phone_number',
            'email',
        ]
        widgets = {

            'residence_address': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'آدرس محل سکونت', 'rows' : '5'}),
            'residence_address_2': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'آدرس دوم محل سکونت', 'rows' : '5'}),
            'residence_work': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'آدرس محل کار', 'rows' : '5'}),
            'residence_postcode': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد پستی محل سکونت', 'maxlength': '10'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن', 'maxlength': '11'}),
            'emergency_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن اظطراری', 'maxlength': '11'}),
            'home_phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن منزل', 'maxlength': '11'}),
            'email' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
        }

    def clean_residence_address(self):
        residence_address = self.cleaned_data.get('residence_address')
        if not residence_address:
            raise forms.ValidationError("این فیلد اجباری است.")
        return residence_address

    def clean_residence_address_2(self):
        residence_address_2 = self.cleaned_data.get('residence_address_2')
        if not residence_address_2:
            raise forms.ValidationError("این فیلد اجباری است.")
        return residence_address_2

    def clean_residence_work(self):
        residence_work = self.cleaned_data.get('residence_work')
        if not residence_work:
            raise forms.ValidationError("این فیلد اجباری است.")
        return residence_work

    def clean_residence_postcode(self):
        residence_postcode = self.cleaned_data.get('residence_postcode')
        if not residence_postcode:
            raise forms.ValidationError("این فیلد اجباری است.")
        return residence_postcode

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("این فیلد اجباری است.")
        return phone_number

    def clean_emergency_phone_number(self):
        emergency_phone_number = self.cleaned_data.get('emergency_phone_number')
        if not emergency_phone_number:
            raise forms.ValidationError("این فیلد اجباری است.")
        return emergency_phone_number

    def clean_home_phone_number(self):
        home_phone_number = self.cleaned_data.get('home_phone_number')
        if not home_phone_number:
            raise forms.ValidationError("این فیلد اجباری است.")
        return home_phone_number


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("این فیلد اجباری است.")
        return email


class CooperationFormStep3(forms.ModelForm):
    class Meta:
        model = Cooperate
        fields = [
            'professional_certificates',
            'skills',
        ]
        widgets = {

            'professional_certificates': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'اگر گواهینامه فنی حرفه ای خاصی دارید توضیح دهید', 'rows' : '5'}),
            'skills': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'اگر مهارت خاصی دارید توضیح دهید', 'rows' : '5'}),

        }
    def clean_professional_certificates(self):
        professional_certificates = self.cleaned_data.get('professional_certificates')
        if not professional_certificates:
            raise forms.ValidationError("این فیلد اجباری است.")
        return professional_certificates

    def clean_skills(self):
        skills = self.cleaned_data.get('skills')
        if not skills:
            raise forms.ValidationError("این فیلد اجباری است.")
        return skills


class CooperationFormStep4(forms.ModelForm):
    class Meta:
        model = Cooperate
        fields = [
            'mental_physical_status',
            'requested_salary',
        ]
        widgets = {

            'mental_physical_status': forms.Textarea(attrs={'class': 'message-field', 'placeholder': 'وضعیت روحی و جسمانی خود را تعریف کنید', 'rows' : '3'}),
            'requested_salary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'حقوق درخواستی', 'maxlength': '10'}),

        }
    def clean_mental_physical_status(self):
        mental_physical_status = self.cleaned_data.get('mental_physical_status')
        if not mental_physical_status:
            raise forms.ValidationError("این فیلد اجباری است.")
        return mental_physical_status

    def clean_requested_salary(self):
        requested_salary = self.cleaned_data.get('requested_salary')
        if not requested_salary:
            raise forms.ValidationError("این فیلد اجباری است.")
        return requested_salary