from django.urls import path
from . import views
app_name = "store"

urlpatterns = [
	path('company_info/<int:company_id>', views.CompanyDetail, name='company_info'),
	path('<int:company_id>/brand_info/<int:brand_id>', views.BrandDetail, name='brand_info'),
]