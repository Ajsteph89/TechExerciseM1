from django.urls import path
from techex import views


urlpatterns = [

    path('entries/search/', views.EntryList.as_view(), name='id-search'),

]
