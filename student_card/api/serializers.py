from rest_framework import serializers
from .models import StudentCard

class StudentCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCard
        fields = '__all__'

# usado para validar e manipular dados na API de forma eficiente.