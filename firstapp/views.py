import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from firstapp.models import FirstCurriculum

# Create your views here.


def insert(request):
    FirstCurriculum.objects.create(name="french")
    FirstCurriculum(name='science').save()

    return HttpResponse('data is inserted')


def show(request):
    curriculum = FirstCurriculum.objects.all()

    return render(
        request, 'firstapp/show.html',
        {'curriculum_items': curriculum})


def req_get(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET['c']
    result = '%s %s %s' % (a, b, c)
    return HttpResponse(result)


@csrf_exempt
def req_post(request):
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST['c']
        result = '%s %s %s' % (a, b, c)
        return HttpResponse(result)
    return render(request, 'firstapp/post.html')


def req_ajax4(request):

    return render(request, 'firstapp/ajax4.html')


@csrf_exempt
def req_json(request):
    obj = request.body.decode("utf-8")
    data = json.loads(obj)
    return JsonResponse(data)
