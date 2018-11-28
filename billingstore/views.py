from django.shortcuts import render, get_object_or_404
from .models import Company, Brand

def CompanyDetail(request,company_id):
	detail_company = get_object_or_404(Company,pk=company_id)
	return render(request,'billingstore/company_detail.html',{'company': detail_company})

def BrandDetail(request, company_id, brand_id):
	detail_brand = get_object_or_404(Brand,pk=brand_id)
	return render(request,'billingstore/brand_detail.html',{'brand':detail_brand })
