from .views import *
from django.urls import path, include

urlpatterns = [
    path('', index, name='home'),
    path('sobre', sobre, name='sobre'),
    path('contato', contato, name='contato'),

]