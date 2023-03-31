from django.shortcuts import render
from .models import Entry
from .serializers import EntrySerializer
from rest_framework import generics
from rest_framework import filters
# Create your views here.


# view for endpoint to allow search by Id field
class IdSearchList(generics.ListAPIView):
    search_fields = ['Id']
    filter_backends = (filters.SearchFilter,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


# view for endpoint to allow search by account number
class AccountSearchList(generics.ListAPIView):
    search_fields = ['AccountNumber']
    filter_backends = (filters.SearchFilter,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

# view for date search 
class DateSearchList(generics.ListAPIView):
    search_fields = ['EffectiveDate', 'PostDate', 'ActivityDate' ]
    # override built in filter to allow for searching date ranges
    filter_backends = (filters.SearchFilter,)
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


# Setting up a dynamic search filter for searching by any field or multiples

# override built in search filters
# class DynamicSearchFilter(filters.SearchFilter):
#     def get_search_fields(self, view, request):
#         return request.GET.getlist('search_fields', [])

# class AnySearchList(generics.ListAPIView):
#     filter_backends = (DynamicSearchFilter,)
#     queryset = Entry.objects.all()
#     serializer_class = EntrySerializer






