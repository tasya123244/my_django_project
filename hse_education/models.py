from django.db import models

class StudentProfile(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField("Фото", upload_to='profile/')
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    resume = models.FileField("Резюме", upload_to='resumes/')

class EducationalProgram(models.Model):
    title = models.CharField("Название", max_length=200)
    url = models.URLField("Ссылка на программу")
    description = models.TextField("Описание")
    skills = models.TextField("Чему научусь")
    advantages = models.TextField("Преимущества")
    prospects = models.TextField("Перспективы")

class ProgramManager(models.Model):
    ROLE_CHOICES = [
        ('head', 'Академический руководитель'),
        ('manager', 'Менеджер программы'),
    ]
    full_name = models.CharField("ФИО", max_length=100)
    role = models.CharField("Роль", max_length=10, choices=ROLE_CHOICES)
    photo = models.ImageField("Фото", upload_to='managers/')
    email = models.EmailField("Email")

class Classmate(models.Model):
    full_name = models.CharField("ФИО", max_length=100)
    photo = models.ImageField("Фото", upload_to='classmates/')
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)