from django.shortcuts import render
from .models import Entry
from .serializers import EntrySerializer
from rest_framework import generics
# Create your views here.


class EntryList(generics.ListAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer