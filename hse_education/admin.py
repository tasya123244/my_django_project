from django.contrib import admin

# Register your models here.
from .models import StudentProfile, EducationalProgram, ProgramManager, Classmate

admin.site.register(StudentProfile)
admin.site.register(EducationalProgram)
admin.site.register(ProgramManager)
admin.site.register(Classmate)