from django.shortcuts import render
from .models import StudentProfile, EducationalProgram, ProgramManager, Classmate
from django.db.models import Q

def profile_page(request):
    profile = StudentProfile.objects.first()
    return render(request, 'profile.html', {'profile': profile})

def program_page(request):
    program = EducationalProgram.objects.first()
    return render(request, 'program.html', {'program': program})

def management_page(request):
    managers = ProgramManager.objects.all()
    return render(request, 'management.html', {'managers': managers})

def classmates_page(request):
    # Получаем параметры
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort', 'full_name')
    
    # Настройки сортировки
    valid_sort_fields = {
        'full_name': 'ФИО (А-Я)',
        '-full_name': 'ФИО (Я-А)',
    }
    
    # Фильтрация и сортировка
    classmates = Classmate.objects.all()
    
    # Поиск по фамилии (или части ФИО)
    if search_query:
        classmates = classmates.filter(
            Q(full_name__icontains=search_query)
        )
    
    # Сортировка
    if sort_by in valid_sort_fields:
        classmates = classmates.order_by(sort_by)
    
    context = {
        'classmates': classmates,
        'sort_options': valid_sort_fields,
        'current_sort': sort_by,
        'search_query': search_query,
    }
    return render(request, 'classmates.html', context)