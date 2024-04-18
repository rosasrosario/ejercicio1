from django.shortcuts import render

# Create your views here.
from.serializer import InstrumentoSer
from .models import Instrumento
from rest_framework import viewsets

class InstrumentoViews(viewsets.ModelViewSet):
    queryset=Instrumento.objects.all()
    serializer_class=InstrumentoSer