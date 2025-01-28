from django.forms import ValidationError
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentProfileForm, CourseSelectionForm
from accounts.models import Student
from .models import Course
from .services import EnrollmentService
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.exceptions import ValidationError




class Home(View):
    def get(self, request):
        return render(request, 'course/home.html')


class StudentProfileView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            context = {
                'student': student,
                'readonly_fields': {
                    'شماره دانشجویی': student.student_number,
                    'ایمیل': student.email,
                    'کد ملی': student.national_id,
                    'سال ورود': student.admission_year,
                }
            }
            return render(request, 'course/profile.html', context)
        except Student.DoesNotExist:
            messages.error(request, 'پروفایل دانشجویی یافت نشد')
            return redirect('home')


class StudentProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
            form = StudentProfileForm(instance=student)
            return render(request, 'course/profile_edit.html', {'form': form})
        except Student.DoesNotExist:
            messages.error(request, 'پروفایل دانشجویی یافت نشد')
            return redirect('home')
    
    def post(self, request):
        try:
            student = Student.objects.get(user=request.user)
            form = StudentProfileForm(request.POST, instance=student)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'اطلاعات با موفقیت به‌روزرسانی شد')
                return redirect('student_profile')
            
            return render(request, 'course/profile_edit.html', {'form': form})
            
        except Student.DoesNotExist:
            messages.error(request, 'پروفایل دانشجویی یافت نشد')
            return redirect('home')


@login_required
def course_selection_view(request):
    form = CourseSelectionForm()
    return render(request, 'course/course_selection.html', {
        'form': form
    })


@login_required
def get_department_courses(request):
    department_id = request.GET.get('department_id')
    if department_id:
        courses = Course.objects.filter(
            department_id=department_id,
            capacity__gt=0
        ).values('id', 'name', 'code', 'credits', 'instructor__first_name',
                'instructor__last_name', 'capacity', 'initial_capacity')
        return JsonResponse({'courses': list(courses)})
    return JsonResponse({'courses': []})


@login_required
@require_POST
def enroll_course(request):
    course_id = request.POST.get('course_id')
    try:
        course = Course.objects.get(id=course_id)
        student = Student.objects.get(user=request.user)
        
        # استفاده از سرویس برای ثبت‌نام
        EnrollmentService.enroll_student(student, course)

        
        messages.success(request, f'درس {course.name} با موفقیت اضافه شد.')
        return JsonResponse({
            'status': 'success',
            'message': f'درس {course.name} با موفقیت اضافه شد.'
        })
        
    except Course.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'درس مورد نظر یافت نشد.'
        }, status=404)
    except ValidationError as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)