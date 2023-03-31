from django.urls import path
from techex import views


urlpatterns = [
    # url for searching by Id
    path('entries/id/', views.IdSearchList.as_view(), name='id-search'),
    
    #url for searching by AccountNumber
    path('entries/account/', views.AccountSearchList.as_view(), name='account-search'),

    #url for searching by Dates
    path('entries/dates/', views.DateSearchList.as_view(), name='account-search'),

    # search by any field
    # path('entries/any/', views.AccountSearchList.as_view(), name='any-search'),
]
