from django.shortcuts import render_to_response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics


# Create your views here.


def fb_view(request):
    return render_to_response('facebook.html')


class SnippetList(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
