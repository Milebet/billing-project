from django.urls import path
from . import views

urlpatterns = [
	path('index_division/',views.index_division, name='index_division'),
	path('add_division/',views.add_division, name='add_division'),
	path('register_product/',views.RegisterProduct, name='register_product'),
	path('index_products/',views.IndexProducts, name='index_products'),
	path('stock/',views.CurrentStock, name='stock'),
	path('damaged_products/',views.DamagedProducts, name='damaged_products'),
]