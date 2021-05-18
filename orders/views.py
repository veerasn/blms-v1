from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import viewsets

from .models import Person, HumanName
from .serializers import PersonSerializer, HumanNameSerializer


# Create your views here
class PersonItemViewSet(viewsets.ModelViewSet):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


@csrf_exempt
def personApi(request, id=0):
    if request.method == 'GET':
        person = Person.objects.all()
        person_serializer = PersonSerializer(person, many=True)
        return JsonResponse(person_serializer.data, safe=False)

    elif request.method == 'POST':
        person_data = JSONParser().parse(request)
        person_serializer = PersonSerializer(data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse('Record saved successfully!', safe=False)
        return JsonResponse('Failed to add record.', safe=False)

    elif request.method == 'PUT':
        person_data = JSONParser().parse(request)
        person = Person.objects.get(id=person_data['id'])
        person_serializer = PersonSerializer(person, data=person_data)
        if person_serializer.is_valid():
            person_serializer.save()
            return JsonResponse('Record updated successfully!', safe=False)
        return JsonResponse('Failed to update record.', safe=False)

    elif request.method == 'DELETE':
        person = Person.objects.get(id=id)
        person.delete()
        return JsonResponse('Record deleted successfully!', safe=False)


def index(request):
    person_list = Person.objects.all()
    context = {
        'person_list': person_list
    }
    return render(request, 'orders/index.html', context)


def detail(request, person_id):
    return HttpResponse('You are looking at details of person with id %s' % person_id)


def patient(request, person_id):
    return HttpResponse('You are looking at patient list of person with id %s' % person_id)


def order(request, patient_id):
    return HttpResponse('You are looking at orders associated with patient with %s' % patient_id)
