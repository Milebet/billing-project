from django.urls import path
from . import views 

urlpatterns = [
	path('search_payment/', views.SearchPayment, name='search_payment')
]