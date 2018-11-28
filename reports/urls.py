from django.urls import path
from . import views

urlpatterns = [
	path('generate_report/', views.CreateReport, name='generate_report'),
	path('downloaded_reports/', views.DownloadedReports, name='downloaded_reports'),
]