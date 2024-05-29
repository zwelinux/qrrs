from django.contrib import admin
from .models import * 
from django.contrib.auth.models import User, Group

admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Faculty)



class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'subject', 'student', 'date', 'rollcall']
    list_filter = ['subject', 'student', 'date']
    

admin.site.register(Attendance, AttendanceAdmin)    

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'QRRS'
admin.site.site_title = 'QRRS'