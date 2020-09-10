from django.urls import path
from . import views

urlpatterns= [
	path('home', views.HomePageView.as_view(), name='home'),
        path('', views.HomePageView.as_view(), name='home'),
        path('success', views.SuccessPageView.as_view() , name='success'),
]
