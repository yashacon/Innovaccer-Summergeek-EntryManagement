from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='HOME'),
    path('app/',views.app,name='checkin')
]