from django.shortcuts import render
from django.http import HttpResponseForbidden
from . import dia, models
import math

def index(request):
    return render(request, "main/index.html", {})

def results(request):
    if request.method != 'POST':
        return HttpResponseForbidden('FORBIDDEN: only post method allowed')
    data = {
        'Спорт и здоровье': 3,
        'Семья': 9,
        'Друзья': 8,
        'Работа': 6,
        'Хобби': 7,
        'Финансы': 9,
        'Саморазвитие': 10
    }
    sum = 0
    for i in range(1, 8):
        sum += int(request.POST[f'range{i}'])
    data['Спорт и здоровье'] = int(request.POST[f'range6'])
    data['Семья'] = int(request.POST[f'range1'])
    data['Друзья'] = int(request.POST[f'range2'])
    data['Работа'] = int(request.POST[f'range3'])
    data['Хобби'] = int(request.POST[f'range4'])
    data['Финансы'] = int(request.POST[f'range5'])
    data['Саморазвитие'] = int(request.POST[f'range7'])
    text = ''
    if sum < 30:
        text = 'Тебе необходим заряд положительных эмоций. Пройди мастер-класс на «Пикнике» или побалуй себя на фуд-корте!'
    elif sum >= 30 and sum < 50:
        text = 'Ты счастливый человек, поделись своей улыбкой на нашей фотозоне!'
    elif sum >= 50:
        text = 'Ты переполнен счастьем и готов делиться с другими. Заряди энергией всех вокруг и оторвись на «Пикнике» по полной!'
    dia.generate(data)
    v = models.Vote.objects.create(range1=int(request.POST[f'range1']), range2=int(request.POST[f'range2']),
                                   range3=int(request.POST[f'range3']), range4=int(request.POST[f'range4']),
                                   range5=int(request.POST[f'range5']), range6=int(request.POST[f'range6']),
                                   range7=int(request.POST[f'range7']))
    v.name = request.POST['name']
    v.save()
    return render(request, "main/results.html", {'text': text})

def admin(request):
    data = models.Vote.objects.all()
    r1, r2, r3, r4, r5, r6, r7 = 0, 0, 0, 0, 0, 0, 0
    c1, c2, c3, c4, c5, c6, c7 = 0, 0, 0, 0, 0, 0, 0
    n = False
    for i in data:
        n = True
        c1 += 1
        r1 += i.range1
        c2 += 1
        r2 += i.range2
        c3 += 1
        r3 += i.range3
        c4 += 1
        r4 += i.range4
        c5 += 1
        r5 += i.range5
        c6 += 1
        r6 += i.range6
        c7 += 1
        r7 += i.range7
    if not n:
        data = {
            'Спорт и здоровье': 1,
            'Семья': 1,
            'Друзья': 1,
            'Работа': 1,
            'Хобби': 1,
            'Финансы': 1,
            'Саморазвитие': 1
        }
    else:
        data = {
            'Спорт и здоровье': math.floor(r1/c1),
            'Семья': math.floor(r2/c2),
            'Друзья': math.floor(r3/c3),
            'Работа': math.floor(r4/c4),
            'Хобби': math.floor(r5/c5),
            'Финансы': math.floor(r6/c6),
            'Саморазвитие': math.floor(r7/c7)
        }
    dia.generate(data)
    return render(request, "main/admin.html", {})