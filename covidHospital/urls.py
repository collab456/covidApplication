from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    #ath('add', views.add, name = 'add')
    path('search', views.search, name = 'search'),
    path('book', views.book, name = 'book'),
    path('cancel', views.cancel, name = 'cancel')
]
