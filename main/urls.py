from . import views
from django.urls import path
urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.index_2, name='about')
]