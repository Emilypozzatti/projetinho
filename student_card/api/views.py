from django.shortcuts import render
from rest_framework import viewsets
from .models import StudentCard
from .serializers import StudentCardSerializer

class StudentCardViewSet(viewsets.ModelViewSet):
    queryset = StudentCard.objects.all()
    serializer_class = StudentCardSerializer

# define a API para o modelo