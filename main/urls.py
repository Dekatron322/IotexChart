from django.urls import path
from . import views

app_name = "main"

urlpatterns = [

	path("", views.IndexView, name="index"),

	path("banner/", views.BannerView, name="banner"),

	path("unvetted/", views.unvetted, name="unvetted"),
	path('verify/banner/<int:pk>/', views.VerifyBannerView, name="verify_banner"),
	path('verify/vetted/<int:pk>/', views.VerifyVettedView, name="verify_vetted"),


	path('all-banner/', views.AllBannerView, name="all_banner"),

	path('all-vetted/', views.AllVettedView, name="all_vetted"),

]

