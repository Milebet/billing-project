from django.urls import path
from . import views
app_name = "store"

urlpatterns = [
	path('<int:company_id>', views.CompanyDetail, name='company_info'),
	path('edit/<int:company_id>', views.edit_company, name='edit_company'),
	path('<int:company_id>/brand/<int:brand_id>', views.BrandDetail, name='brand_info'),
	path('<int:company_id>/brand/edit/<int:brand_id>', views.edit_brand, name='edit_brand'),
]