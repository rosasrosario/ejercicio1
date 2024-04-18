from rest_framework import serializers
from .models import Instrumento

class InstrumentoSer(serializers.ModelSerializer):
    class Meta:
        model = Instrumento
        fields = '__all__'
    