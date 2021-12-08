from django.contrib import messages
from django.shortcuts import (HttpResponse, HttpResponseRedirect,
                              get_object_or_404, redirect, render)
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import *
from .models import *




from django.core.mail import send_mail

from datetime import datetime
import datetime as dt
import requests

#from .forms import UserForm

from datetime import datetime
from requests import Request, Session
import json
import time
from datetime import datetime, timedelta



def GetData():
	apiUrl = "https://api.pro.coinbase.com"
	sym = "IOTX-USD"
	barSize = "60"

	timeEnd = datetime.now()
	delta = timedelta(seconds=int(barSize))

	timeStart = timeEnd - (1*delta)

	timeStart = timeStart.isoformat()
	timeEnd = timeEnd.isoformat()

	parameters = {
		"start": timeStart,
		"end": timeEnd,
		"granularity": "60",
	}
	headers = {"content-type": "application/json"}

	data = requests.get(f"{apiUrl}/products/{sym}/candles",
			params=parameters,
			headers=headers).json()

	return data

def IndexView(request):
	if request.method == "POST":
		pass


	else:
		banner = Banner.objects.all().order_by('-pub_date')[:4]
		side_banner = Banner.objects.all().order_by('-pub_date')[5:7]
		aside_banner = Banner.objects.all().order_by('-pub_date')[8:10]
		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=1").json()
		#data = GetData()
		data1 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data1.append(new_list)


		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=7").json()
		#data = GetData()
		data7 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data7.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=14").json()
		#data = GetData()
		data14 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data14.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=30").json()
		#data = GetData()
		data30 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data30.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=90").json()
		#data = GetData()
		data90 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data90.append(new_list)


		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=180").json()
		#data = GetData()
		data180 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data180.append(new_list)

		#1day chart
		response = requests.get("https://api.coingecko.com/api/v3/coins/iotex/ohlc?vs_currency=usd&days=365").json()
		#data = GetData()
		data365 = []

		for item in response:
			new_list = []
			new_list.append(item[0])
			new_list.append(item[1])
			new_list.append(item[2])
			new_list.append(item[3])
			new_list.append(item[4])

			data365.append(new_list)

		context = {"banner": banner, "side_banner":side_banner, "aside_banner":aside_banner, "data1": data1, "data7": data7, "data14": data14, "data30": data30, "data90": data90, "data180": data180, "data365": data365}
		return render(request, "main/index.html", context )


def AllBannerView(request):

	#url = "https://iotexscan.io/api/getInitData"

	#payload={}
	#headers = {}

	#response = requests.request("GET", url, headers=headers, data=payload)
	banner = Banner.objects.all().order_by('-pub_date')


	context = {
		
		"banner": banner,
		#"response":response,

        }

	return render(request, "main/allbanner.html", context )


def VerifyBannerView(request, pk):
	banner = Banner.objects.get(id=pk)
	context = {
        "banner":banner
    	}
	#form = VerifyBannerForm(request.POST or None)
	if request.method == "POST":
		banner = Banner.objects.get(id=pk)
		banner.status = True
		banner.save()
			
		messages.success(request, 'updated')
		#return HttpResponseRedirect(reverse("main:verify_banner"))
		#return redirect(reverse('verify_banner'))

	else:
		pass

	return render(request, 'main/verify_banner.html', context)


def BannerView(request):
	form = BannerForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == "POST":
		if form.is_valid():
			title = form.cleaned_data.get('title')
			text = form.cleaned_data.get('text')
			link = form.cleaned_data.get('link')
			company_name = form.cleaned_data.get('company_name')
			image = request.FILES['image']
			interest = form.cleaned_data.get('interest')
			budget = form.cleaned_data.get('budget')
			proof_of_payment = form.cleaned_data.get('proof_of_payment')
			about_project = form.cleaned_data.get('about_project')

			try:
				form = Banner()
				form.title = title
				form.text  = text 
				form.link = link
				form.company_name = company_name
				form.image = image
				form.interest = interest
				form.budget = budget
				form.proof_of_payment = proof_of_payment
				form.about_project = about_project
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/banner.html", context)
			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')
	return render(request, "main/banner.html", context )

def unvetted(request):
	form = UnvettedForm(request.POST, request.FILES)
	context = {'form': form}
	if request.method == 'POST':
		if form.is_valid():
			token_address = form.cleaned_data.get('token_address')
			telegram_url = form.cleaned_data.get('telegram_url')
			#proof_of_payment = form.cleaned_data.get("proof_of_payment")
			image = request.FILES['image']

			try:
				form = Unvetted()
				form.token_address = token_address
				form.telegram_url = telegram_url
				#proof_of_payment = proof_of_payment
				form.image = image
				form.save()
				messages.success(request, "Submitted Successfully")
				return render(request, "main/unvetted.html", context)

			except Exception as e:
				messages.error(request, 'Could Not Add ' + str(e))

		else:
			messages.error(request, 'Fill Form Properly ')

	return render(request, "main/unvetted.html", context)

def AllVettedView(request):
	vetted = Unvetted.objects.all().order_by('-pub_date')

	context = {	
		"vetted": vetted,
        }

	return render(request, "main/allvetted.html", context )

def VerifyVettedView(request, pk):
	vetted = Unvetted.objects.get(id=pk)

		

	context = {
        "vetted":vetted, 
        "response":response,
    	}
	if request.method == "POST":
		vetted = Unvetted.objects.get(id=pk)
		vetted.status = True
		vetted.save()
			
		messages.success(request, 'updated')

	else:
		pass

	return render(request, 'main/verify_vetted.html', context)



	