from django import forms
from accounts.models import Student


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'phone_number', 'major']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'phone_number': 'شماره تماس',
            'major': 'رشته تحصیلی',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError("شماره تماس نمی تواند خالی باشد.")
        elif not str(phone_number).isdigit() or len(str(phone_number)) != 11:
            raise forms.ValidationError("شماره تماس باید ۱۱ رقم باشد و تنها شامل اعداد باشد.")
        return phone_number

