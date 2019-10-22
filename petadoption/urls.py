from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('register/', views.pet_register, name='pet_register'),
    path('adoption_explore/', views.adoption_explore, name='adoption_explore'),
    url(r'pet_info/(?P<pet_id>\d+)/$', views.pet_info, name='pet_info'),
    url(r'^delete_pet/(?P<pet_id>\d+)/$', views.delete_pet, name='delete_pet')
    # path('pet_info/(?P<pet_id>\d+)/$', views.pet_info, name='pet_info'),
    # url(r'adoptionrequest/(?P<pet_id>d+)/$', views.pet_adoption_request, name='pet_adoption_request')
]
