from django.db import models 

class Student(models.Model):
    student_name = models.CharField(max_length=255)
    student_image = models.ImageField(upload_to='images', blank=True, null=True)
    student_roll = models.IntegerField()
    student_year = models.IntegerField()
    student_email = models.EmailField(blank=True, null=True)
    student_phone = models.CharField(max_length=255, blank=True, null=True)
    student_address = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.student_name

class Subject(models.Model):
    subject_name = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=255)
    
    def __str__(self):
        return self.subject_name

class Faculty(models.Model):
    faculty_name = models.CharField(max_length=255)
    faculty_rank = models.CharField(max_length=255)
    faculty_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.faculty_name
    
    class Meta:
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'
    
class Attendance(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.date.day+1) + "." + str(self.date.month) + "." + str(self.date.year)    

    def rollcall(self):
        return "<h1>{{ rollCount }}</h1>"
