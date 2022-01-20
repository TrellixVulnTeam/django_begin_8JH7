
from django.forms.models import model_to_dict
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Tables
import secondapp.models as models
from .models import ArmyShop, Course, Curriculum
# Create your views here.


def main(request):
    return HttpResponse('<u>Main</u>')


def insert(request):
    # 1. create()
    # 테이블에 값을 넣어줌
    Curriculum.objects.create(name="linux")

    # 2.save()
    c = Curriculum(name='python')
    c.save()

    Curriculum(name='python').save()
    Curriculum(name='django').save()

    return HttpResponse('ok')


def insertCourse(request):
    # 1.create()
    Course.objects.create(name='eng', cnt=1313)

    # 2.save()
    c = Course(name='math', cnt=12)
    c.save()
    # or
    Course(name='history', cnt=131).save()

    return HttpResponse('ok')


def show(request):
    course = Course.objects.all()

    return render(request, 'secondapp/show.html',
                  {'course_items': course})


def showCourse(request):
    course = Course.objects.all()
    result = ''

    for item in course:
        result += item.name + "<br>"

    return HttpResponse(result)


def armyShop(request):
    items = ArmyShop.objects.all()

    return render(request, 'secondapp/armyshop_table.html',
                  {'itemList': items})


def army_shop_path(request, year, month):
    items = ArmyShop.objects.filter(year=year, month=month)
    # formatting 방식 3가지
    #result = ''
    # for i in items:
    #     result += '%s %s %s<br>' % (i.year, i.month, i.name)

    # list comprehension
    result = ['%s %s %s<br>' % (i.year, i.month, i.name) for i in items]

    return HttpResponse(''.join(result))


def army_shop_query(request):
    prd = request.GET.get('prd', '')
    items = ArmyShop.objects.filter(name__contains=prd).order_by('-year')

    # result = ['%s %s %s %s %s<br>' %
    #           (i.id, i.year, i.month, i.type, i.name) for i in items]
    # result = [
    #     f"{i.id}, {i.year}, {i.month}, {i.type}, {i.name}<br>" for i in items]

    return render(request, 'secondapp/armyshop_table.html',
                  {'itemList': items})


@csrf_exempt
def ajax_get(request):
    allCourse = Course.objects.all()

    data = []
    for a in allCourse:
        #d = model_to_dict(a)
        data.append(model_to_dict(a))

    return JsonResponse(data, safe=False)


def ajax_Exam(request):
    return render(request, 'secondapp/ajax_exam.html')
