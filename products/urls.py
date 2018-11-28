from django.urls import path
from . import views

urlpatterns = [
	path('index_division/',views.index_division, name='index_division'),
	path('add_division/',views.add_division, name='add_division'),
	path('index_lines/',views.index_lines, name='index_lines'),
	path('add_lines/',views.add_lines, name='add_lines'),
	path('index_category/',views.index_category, name='index_category'),
	path('add_category/',views.add_category, name='add_category'),
	path('index_unit/',views.index_unit, name='index_unit'),
	path('add_unit/',views.add_unit, name='add_unit'),
	path('index_equivalence/',views.index_equivalence, name='index_equivalence'),
	path('add_equivalence/',views.add_equivalence, name='add_equivalence'),
	path('register_product/',views.RegisterProduct, name='register_product'),
	path('index_products/',views.IndexProducts, name='index_products'),
	path('stock/',views.CurrentStock, name='stock'),
	path('damaged_products/',views.DamagedProducts, name='damaged_products'),
]