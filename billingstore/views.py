from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CompanyForm, BrandForm
from .models import Company, Brand
from django.contrib import messages 

@login_required()
def CompanyDetail(request,company_id):
	detail_company = get_object_or_404(Company,id=company_id)
	return render(request,'billingstore/company_detail.html',{'company': detail_company})

@login_required()
def BrandDetail(request, company_id, brand_id):
	detail_company = Company.objects.get(id=company_id)
	detail_brand = detail_company.brand_set.get(id=brand_id)
	#detail_brand = get_object_or_404(Brand,id=brand_id)
	return render(request,'billingstore/brand_detail.html',{'company':detail_company ,'brand':detail_brand })

def edit_company(request, company_id):
	if (request.user.groups.filter(name='Administrador').exists()):
		company = Company.objects.get(id=company_id)
		if request.method == 'POST':
			form = CompanyForm(request.POST, instance=company)
			if form.is_valid():
				form.save()
				messages.success(request,('Los datos de la empresa han sido actualizados...'))
				return redirect('store:company_info', company.id)
			else:
				messages.error(request,('Something went wrong'))
				form = CompanyForm(request.POST, instance=company)
		else:
			form = CompanyForm(instance=company)
		
		context = {'form': form, 'company_id': company_id}
		return render(request, 'billingstore/edit_company.html',context)
	else:
		messages.error(request,"Permission denied of your role")
		return redirect('home')

def edit_brand(request, company_id, brand_id):
	if (request.user.groups.filter(name='Administrador').exists()):
		company = Company.objects.get(id=company_id)
		brand = company.brand_set.get(id=brand_id)
		if request.method == 'POST':
			form = BrandForm(request.POST, instance=brand)
			if form.is_valid():
				form.save()
				messages.success(request,('Los datos de la sucursal han sido actualizados...'))
				return redirect('store:brand_info',company.id, brand.id)
			else:
				messages.error(request,('Something went wrong'))
				form = BrandForm(request.POST, instance=brand)
		else:
			form = BrandForm(instance=brand)
		
		context = {'form': form, 'company_id': company_id, 'brand_id':brand_id}
		return render(request, 'billingstore/edit_brand.html',context)
	else:
		messages.error(request,"Permission denied of your role")
		return redirect('home')