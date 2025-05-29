from django.shortcuts import render, redirect
from django.http import HttpResponse
from urllib.parse import unquote
from django.db.models import Count, Avg, Min, Max
from .forms import AbcModelForm
from .models import AbcModel
from .filters import AbcModelFilter

def xyz_form(request):
    if request.method == "POST":
        form = AbcModelForm(request.POST)
        if form.is_valid():
            instance = form.save()  
            return redirect("BodrovaApp:xyz_result", pk=instance.pk)
    else:
        form = AbcModelForm()
    return render(request, "xyz_form.html", {"form": form})



def xyz_result(request, pk):
    try:
        obj = AbcModel.objects.get(pk=pk)
    except AbcModel.DoesNotExist:
        return render(request, "xyz_result.html", {"error": "Запись не найдена"})

    context = {
        "last_row": {
            "full_name": obj.full_name,
            "x": obj.x,
            "y": obj.y,
            "final_score": obj.final_score,
            "result": obj.result,
        }
    }
    return render(request, "xyz_result.html", context)


def xyz_result_all(request):
    all_objects = AbcModel.objects.all().order_by("-id")

    if not all_objects.exists():
        return render(request, "xyz_result_all.html", {"error": "Нет данных"})

    data_for_table = []

    for obj in all_objects:
        if obj.final_score != 0.5 * obj.x + 0.5 * obj.y:
            obj.final_score = 0.5 * obj.x + 0.5 * obj.y
            obj.result = f"Итоговая оценка: {obj.final_score}"
            obj.save(update_fields=["final_score", "result"])

        data_for_table.append({
            "id": obj.id,
            "full_name": obj.full_name,
            "x": obj.x,
            "y": obj.y,
            "final_score": obj.final_score,
            "result": obj.result,
            "current_date": obj.current_date,
        })

    return render(request, "xyz_result_all.html", {"data_for_table": data_for_table})

def xyz_result_filtered(request):
    qs = AbcModel.objects.all()
    filterset = AbcModelFilter(request.GET, queryset=qs)
    filtered_qs = filterset.qs

    sort_order = request.GET.get('sort_score', 'asc')
    filtered_qs = filtered_qs.order_by('-final_score' if sort_order == 'desc' else 'final_score')

    data_for_table = []
    for obj in filtered_qs:
        if obj.final_score != 0.5 * obj.x + 0.5 * obj.y:
            obj.final_score = 0.5 * obj.x + 0.5 * obj.y
            obj.result = f"Итоговая оценка: {obj.final_score}"
            obj.save(update_fields=['final_score', 'result'])

        data_for_table.append({
            "id": obj.id,
            "full_name": obj.full_name,
            "x": obj.x,
            "y": obj.y,
            "final_score": obj.final_score,
            "result": obj.result,
            "current_date": obj.current_date,
        })

    context = {
        "filter": filterset,
        "data_for_table": data_for_table,
        "current_sort": sort_order,
    }
    return render(request, "xyz_result_filtered.html", context)

def stats_view(request):
    stats = AbcModel.objects.aggregate(
    total_records=Count('id'),
    avg_score=Avg('final_score'),
    min_score=Min('final_score'),
    max_score=Max('final_score')

    )
    return render(request, 'stats.html', {'stats': stats})

def index(request):
    cars = [
        {"name": "Porsche 911 GT3", "description": "502 л.с., 3,4 сек.", "img": "images/porsche.jpg"},
        {"name": "Ferrari 812 Competizione", "description": "830 л.с., 2,9 сек.", "img": "images/ferrari.jpg"},
        {"name": "Lamborghini Huracan STO", "description": "631 л.с., 3,0 сек.", "img": "images/lamborghini.jpg"},
        {"name": "McLaren 765LT", "description": "755 л.с., 2,7 сек.", "img": "images/mclaren.jpg"},
    ]
    images = [
        {"src": "images/машина.jpg", "alt": "Porsche"},
        {"src": "images/машина1.jpg", "alt": "Ferrari"},
        {"src": "images/машина2.jpg", "alt": "Lamborghini"},
    ]
    sections = [
        {"id": "cars", "title": "Наши автомобили"},
        {"id": "services", "title": "Наши услуги"},
    ]
    return render(request, 'index.html', {
        'cars': cars,
        'images': images,
        'sections': sections
    })

def our_team(request):
    user_info = {
        "name": "Бодрова Таисия", "photo": "images/я.png",
        "email": "TAbodrova.27@yandex.ru", "phone": "+70124568799"
    }
    program_info = {
        "name": "Программа «Тюнинг+»",
        "description": "Тюнинг — это процесс модификации...",
        "leader1": {"name": "Анна Константиновна", "photo": "images/Аня.jpg", "email": "AK444@yandex.ru"},
        "leader2": {"name": "Софья Сергеевна", "photo": "images/соня.jpg", "email": "SSDollar@yandex.ru"}
    }
    helpers = [
        {"name": "Пикси", "photo": "images/Пикси.jpg", "email": "Piksi@yandex.ru"},
        {"name": "Шах", "photo": "images/Шах.jpg", "email": "Shah@example.com"},
    ]
    return render(request, "our_team.html", {
        "user_info": user_info,
        "program_info": program_info,
        "helpers": helpers
    })

def cars_view(request):
    mlinks = [
        {"url": "https://www.porsche.com/", "type": "text", "label": "Porsche"},
        {"url": "https://www.ferrari.com/", "type": "text", "label": "Ferrari"},
        {"url": "https://www.lamborghini.com/", "type": "image", "img": "images/lamborghini.jpg"}
    ]
    car_brands = ["Porsche", "Ferrari", "Lamborghini"]
    car_categories = {
        "Спортивные авто": ["Porsche 911 GT3", "Ferrari 812", "Lamborghini STO"],
        "Гиперкары": ["McLaren P1", "Bugatti Chiron", "Koenigsegg Jesko"]
    }
    return render(request, 'links.html', {
        'mlinks': mlinks,
        'car_brands': car_brands,
        'car_categories': car_categories
    })

def calculate_z(request, path_value):
    path_elements = path_value.split("/")
    if len(path_elements) != 2:
        return render(request, "zadacha_1.html", {"result_value": "Ошибка: Неверный формат URL"})

    x_data = path_elements[0].split("=")
    y_data = path_elements[1].split("=")
    if x_data[0] != "x" or y_data[0] != "y" or len(x_data) < 2 or len(y_data) < 2:
        return render(request, "zadacha_1.html", {"result_value": "Ошибка в параметрах URL"})

    try:
        x = float(x_data[1])
        y = float(y_data[1])
        result_value = 1 / (x * y) if x != 0 and y != 0 else "Ошибка: деление на ноль"
    except ValueError:
        result_value = "Ошибка: Невозможно преобразовать в число"

    return render(request, "zadacha_1.html", {
        "x_value": x_data[1], "y_value": y_data[1], "result_value": result_value
    })

def count_overtime_entries(request, records, target_day):
    records = unquote(records)
    target_day = unquote(target_day)
    entries = records.split('|')
    count = 0
    for i in entries:
        parts = i.split(',')
        if len(parts) >= 3 and parts[1] == target_day and int(parts[2]) > 0:
            count += 1
    return render(request, "zadacha_2.html", {
        "records": records, "target_day": target_day, "count": count
    })

def about(request):
    return render(request, 'about.html')
