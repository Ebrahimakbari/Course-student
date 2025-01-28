# from django.db import models
# from accounts.models import CustomUser as User


# class Course(models.Model):
#     name = models.CharField(max_length=100)
#     code = models.CharField(max_length=20, unique=True)
#     credits = models.IntegerField()
#     capacity = models.IntegerField()
#     remaining_capacity = models.IntegerField()
#     exam_date = models.DateField()
#     exam_start_time = models.TimeField()
#     exam_end_time = models.TimeField()
#     department = models.ForeignKey('Department', on_delete=models.PROTECT)
#     instructor = models.ForeignKey('Instructor', on_delete=models.PROTECT)
    
#     def __str__(self):
#         return f"{self.code} - {self.name}"
    
#     def get_all_corequisites(self):
#         """Returns all corequisite courses"""
#         return Course.objects.filter(
#             is_corequisite_for__course=self
#         )


# class Department(models.Model):
#     name = models.CharField(max_length=100)
    
#     def __str__(self):
#         return self.name

# class Instructor(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     department = models.ForeignKey(Department, on_delete=models.PROTECT)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
    
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     national_id = models.CharField(max_length=20)
#     phone_number = models.CharField(max_length=20)
#     major = models.CharField(max_length=100)
#     year = models.IntegerField()
#     max_units = models.IntegerField()
#     student_number = models.CharField(max_length=20, unique=True)
#     admission_year = models.IntegerField()
    
#     def __str__(self):
#         return f"{self.student_number} - {self.first_name} {self.last_name}"

# class Classroom(models.Model):
#     name = models.CharField(max_length=100)
#     capacity = models.IntegerField()
#     department = models.ForeignKey(Department, on_delete=models.PROTECT)
    
#     def __str__(self):
#         return self.name


# class Prerequisite(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='prerequisites')
#     required_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='is_prerequisite_for')
    
#     class Meta:
#         unique_together = ['course', 'required_course']

# class Corequisite(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='corequisites')
#     required_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='is_corequisite_for')
    
#     class Meta:
#         unique_together = ['course', 'required_course']

# class CourseSchedule(models.Model):
#     DAYS_OF_WEEK = [
#         (1, 'شنبه'),
#         (2, 'یکشنبه'),
#         (3, 'دوشنبه'),
#         (4, 'سه‌شنبه'),
#         (5, 'چهارشنبه'),
#         (6, 'پنج‌شنبه'),
#         (7, 'جمعه'),
#     ]
    
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='schedules')
#     day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
#     classroom = models.ForeignKey('Classroom', on_delete=models.CASCADE)
    
#     class Meta:
#         unique_together = ['course', 'day_of_week', 'start_time']

# class Enrollment(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('approved', 'Approved'),
#         ('rejected', 'Rejected'),
#     ]
    
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     enrollment_date = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
#     class Meta:
#         unique_together = ['student', 'course']

# class WeeklySchedule(models.Model):
#     DAYS_OF_WEEK = [
#         (1, 'شنبه'),
#         (2, 'یکشنبه'),
#         (3, 'دوشنبه'),
#         (4, 'سه‌شنبه'),
#         (5, 'چهارشنبه'),
#         (6, 'پنج‌شنبه'),
#         (7, 'جمعه'),
#     ]
    
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
#     start_time = models.TimeField()
#     end_time = models.TimeField()
    
#     class Meta:
#         unique_together = ['student', 'course', 'day_of_week']