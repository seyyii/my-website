from django.urls import path
from seyi_web_app import views

app_name = 'seyi_web_app'

urlpatterns = [
    path('about', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),  
    path('contact/', views.contact, name='contact'),
]