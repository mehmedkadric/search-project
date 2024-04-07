from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    # URL pattern for rendering the search form
    path('', views.search, name='search'),

]
