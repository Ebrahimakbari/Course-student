from django import forms
from django.contrib.auth import authenticate
from .models import CustomUser as User
from .models import Student




class StudentRegistrationForm(forms.Form):
    student_number = forms.CharField(
        label='شماره دانشجویی',
    )
    first_name = forms.CharField(label='نام')
    last_name = forms.CharField(label='نام خانوادگی')
    major = forms.CharField(label='رشته تحصیلی', required=True)
    email = forms.EmailField(label='ایمیل')
    national_id = forms.IntegerField(label='شماره ملی')
    admission_year = forms.IntegerField(label='سال ورود')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput)

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if User.objects.filter(student_number=student_number).exists():
            raise forms.ValidationError('این شماره دانشجویی قبلاً ثبت شده است')
        elif not student_number:
            raise forms.ValidationError("شماره دانشجویی نمی تواند خالی باشد.")
        elif not str(student_number).isdigit() or len(str(student_number)) != 9:
            raise forms.ValidationError("شماره دانشجویی باید 9 رقم باشد و تنها شامل اعداد باشد.")
        return student_number

    def clean_national_id(self):
        national_id = self.cleaned_data.get('national_id')
        if Student.objects.filter(national_id=national_id).exists():
            raise forms.ValidationError('این شماره ملی قبلاً ثبت شده است')
        elif not national_id:
            raise forms.ValidationError("شماره ملی نمی تواند خالی باشد.")
        elif not str(national_id).isdigit() or len(str(national_id)) != 10:
            raise forms.ValidationError("شماره ملی باید 10 رقم باشد و تنها شامل اعداد باشد.")
        return national_id
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است')
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('رمز عبور و تکرار آن باید یکسان باشند')
        return cleaned_data


class StudentLoginForm(forms.Form):
    student_number = forms.CharField(label='شماره دانشجویی')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        student_number = cleaned_data.get('student_number')
        password = cleaned_data.get('password')

        if student_number and password:
            user = authenticate(student_number=student_number, password=password)
            if not user:
                raise forms.ValidationError('شماره دانشجویی یا رمز عبور اشتباه است')
            cleaned_data['user'] = user
        return cleaned_data

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if not student_number:
            raise forms.ValidationError("شماره دانشجویی نمی تواند خالی باشد.")
        elif not str(student_number).isdigit() or len(str(student_number)) != 9:
            raise forms.ValidationError("شماره دانشجویی باید 9 رقم باشد و تنها شامل اعداد باشد.")
        return student_number
    

class PasswordResetVerifyForm(forms.Form):
    student_number = forms.CharField(
        label='شماره دانشجویی',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        student_number = cleaned_data.get('student_number')
        email = cleaned_data.get('email')

        if student_number and email:
            user = User.objects.filter(
                student_number=student_number,
                email=email
            ).first()
            
            if not user:
                raise forms.ValidationError('اطلاعات وارد شده صحیح نمی‌باشد')
            
            cleaned_data['user'] = user
        return cleaned_data

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if not student_number:
            raise forms.ValidationError("شماره دانشجویی نمی تواند خالی باشد.")
        elif not str(student_number).isdigit() or len(str(student_number)) != 9:
            raise forms.ValidationError("شماره دانشجویی باید 9 رقم باشد و تنها شامل اعداد باشد.")
        return student_number


class PasswordResetForm(forms.Form):
    new_password = forms.CharField(
        label='رمز عبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    confirm_password = forms.CharField(
        label='تکرار رمز عبور جدید',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError('رمز عبور و تکرار آن باید یکسان باشند')
        return cleaned_data