from django.urls import path
from . import views
app_name = 'products'

urlpatterns = [
	path('index_division/',views.index_division, name='index_division'),
	path('add_division/',views.add_division, name='add_division'),
	path('edit_division/<int:division_id>',views.edit_division, name='edit_division'),
	path('show_division/<int:division_id>',views.show_division, name='show_division'),
	path('index_lines/',views.index_lines, name='index_lines'),
	path('add_lines/',views.add_lines, name='add_lines'),
	path('edit_line/<int:line_id>',views.edit_line, name='edit_line'),
	path('show_line/<int:line_id>',views.show_line, name='show_line'),
	path('index_category/',views.index_category, name='index_category'),
	path('add_category/',views.add_category, name='add_category'),
	path('edit_category/<int:category_id>',views.edit_category, name='edit_category'),
	path('show_category/<int:category_id>',views.show_category, name='show_category'),
	#path('index_unit/',views.index_unit, name='index_unit'),
	#path('add_unit/',views.add_unit, name='add_unit'),
	#path('index_equivalence/',views.index_equivalence, name='index_equivalence'),
	#path('add_equivalence/',views.add_equivalence, name='add_equivalence'),
	#path('register_product/',views.RegisterProduct, name='register_product'),
	#path('index_products/',views.IndexProducts, name='index_products'),
	#path('stock/',views.CurrentStock, name='stock'),
	#path('damaged_products/',views.DamagedProducts, name='damaged_products'),
	#path('add_damagedproduct/',views.add_inactiveproduct, name='add_damagedproduct'),
]