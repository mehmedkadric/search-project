from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.search, name='search'),
    path('upload-data/', views.upload_data, name='upload_data'),

]
