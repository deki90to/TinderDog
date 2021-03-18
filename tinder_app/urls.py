from django.urls import path
from . import views



urlpatterns = [
	path('', views.home, name='home'),
	path('<pk>/details/', views.details, name='details'),
	path('<pk>/edit/', views.edit, name='edit'),
	path('<pk>/delete/', views.delete, name='delete'),
	path('create/', views.create, name='create'),
	path('search/', views.search, name='search'),
]