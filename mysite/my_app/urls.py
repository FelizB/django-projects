from django.urls import path
from . import views


app_name=  'my_app'

urlpatterns= [
    path('', views.first_view,name='first'),
    path('variable/',views.variable_view, name='variable')
]