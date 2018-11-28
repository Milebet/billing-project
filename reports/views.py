from django.shortcuts import render

def CreateReport(request):
	return render(request,'reports/my_reports.html')

def DownloadedReports(request):
	return render(request,'reports/downloaded_reports.html')