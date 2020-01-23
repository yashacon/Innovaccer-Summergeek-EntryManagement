from django.urls import path
from . import views

urlpatterns=[
    path('',views.checkout,name='checkout'),
    path('archive/',views.archive,name='archive'),
    path('<int:pk>/',views.checkingout,name='checking')
]