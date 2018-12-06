from django.shortcuts import render, redirect, get_object_or_404
from .forms import CompanyForm, BrandForm
from .models import Company, Brand
from django.contrib import messages 

def CompanyDetail(request,company_id):
	detail_company = get_object_or_404(Company,id=company_id)
	return render(request,'billingstore/company_detail.html',{'company': detail_company})

def BrandDetail(request, company_id, brand_id):
	detail_company = Company.objects.get(id=company_id)
	detail_brand = detail_company.brand_set.get(id=brand_id)
	#detail_brand = get_object_or_404(Brand,id=brand_id)
	return render(request,'billingstore/brand_detail.html',{'company':detail_company ,'brand':detail_brand })

def update_info_person(request, user_id):
	user = CustomUser.objects.get(id=user_id)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance= user.person )
		if form.is_valid():
			form.save()
			messages.success(request,('You have Edited your Profile...'))
			return redirect('users:personal_info', user.id)
		else:
			messages.error(request,('Something went wrong'))
			form = EditProfileForm(request.POST, instance= user.person)
	else:
		form = EditProfileForm(instance= user.person)
	
	context = {'form': form, 'user_id': user_id}
	return render(request, 'people/edit_info.html',context)

def edit_company(request, company_id):
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

def edit_brand(request, company_id, brand_id):
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