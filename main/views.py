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
from django.contrib.auth.decorators import login_required




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

def StakingView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/staking.html", context)

def YourStakeView(request):
	if request.method == "POST":
		pass
	else:
		
		context = {}
		return render(request, "main/your_stake.html", context)

def WowSwapView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=wowswap&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=wowswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["wowswap"]["usd"])
		market_cap = int(response["wowswap"]["usd_market_cap"])
		hr_vol = str(response["wowswap"]["usd_24h_vol"])
		hr_chg = str(response["wowswap"]["usd_24h_change"])
		last_updated = str(response["wowswap"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		return render(request, "main/wow.html", context)


def ImagicTokenView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=imagictoken&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=imagictoken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["imagictoken"]["usd"])
		market_cap = int(response["imagictoken"]["usd_market_cap"])
		hr_vol = str(response["imagictoken"]["usd_24h_vol"])
		hr_chg = str(response["imagictoken"]["usd_24h_change"])
		last_updated = str(response["imagictoken"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		return render(request, "main/imagictoken.html", context)


def IotexShibaView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iotexshiba&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotexshiba&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["iotexshiba"]["usd"])
		market_cap = int(response["iotexshiba"]["usd_market_cap"])
		hr_vol = str(response["iotexshiba"]["usd_24h_vol"])
		hr_chg = str(response["iotexshiba"]["usd_24h_change"])
		last_updated = str(response["iotexshiba"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		return render(request, "main/iotexshiba.html", context)


def MetanyxView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=metanyx&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metanyx&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["metanyx"]["usd"])
		market_cap = int(response["metanyx"]["usd_market_cap"])
		hr_vol = str(response["metanyx"]["usd_24h_vol"])
		hr_chg = str(response["metanyx"]["usd_24h_change"])
		last_updated = str(response["metanyx"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		return render(request, "main/metanyx.html", context)

def IotexView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=iotex&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["iotex"]["usd"])
		market_cap = int(response["iotex"]["usd_market_cap"])
		hr_vol = str(response["iotex"]["usd_24h_vol"])
		hr_chg = str(response["iotex"]["usd_24h_change"])
		last_updated = str(response["iotex"]["last_updated_at"])
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		return render(request, "main/iotex.html", context)



def ZoomSwapView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=zoomswap&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zoomswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["zoomswap"]["usd"])
		market_cap = int(response["zoomswap"]["usd_market_cap"])
		hr_vol = str(response["zoomswap"]["usd_24h_vol"])
		hr_chg = str(response["zoomswap"]["usd_24h_change"])
		last_updated = str(response["zoomswap"]["last_updated_at"])
		context = {"data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated, "image":image}
		return render(request, "main/zoomswap.html", context)

def GameFantasyTokenView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=game-fantasy-token&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["game-fantasy-token"]["usd"])
		market_cap = int(response["game-fantasy-token"]["usd_market_cap"])
		hr_vol = str(response["game-fantasy-token"]["usd_24h_vol"])
		hr_chg = str(response["game-fantasy-token"]["usd_24h_change"])
		last_updated = str(response["game-fantasy-token"]["last_updated_at"])
		
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		return render(request, "main/gamefantasy.html", context)

def VitalityView(request):
	if request.method == "POST":
		pass
	else:
		response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=vitality&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true").json()
		image = Banner.objects.all().order_by('?')[:1]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vitality&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		price = str(response["vitality"]["usd"])
		market_cap = int(response["vitality"]["usd_market_cap"])
		hr_vol = str(response["vitality"]["usd_24h_vol"])
		hr_chg = str(response["vitality"]["usd_24h_change"])
		last_updated = str(response["vitality"]["last_updated_at"])
		context = {"image":image, "data":data, "price":price, "market_cap":market_cap, "hr_vol":hr_vol, "hr_chg":hr_chg, "last_updated":last_updated}
		return render(request, "main/vitality.html", context)


def IndexView(request):
	if request.method == "POST":
		pass


	else:
		banner = Banner.objects.all().order_by('-pub_date')[:4]
		
		side_banner = Banner.objects.all().order_by('-pub_date')[5:7]
		aside_banner = Banner.objects.all().order_by('-pub_date')[8:10]
		data = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=game-fantasy-token&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		vita = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=vitality&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		zoom = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=zoomswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotex = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotex&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		metanyx = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=metanyx&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		iotexshiba = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=iotexshiba&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		imagictoken = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=imagictoken&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		wow = requests.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=wowswap&order=market_cap_desc&per_page=100&page=1&sparkline=true&price_change_percentage=1h").json()
		

		context = {"banner": banner, "side_banner":side_banner, "aside_banner":aside_banner, "data":data, "vita":vita, "zoom":zoom, "iotex":iotex, "metanyx":metanyx, "iotexshiba":iotexshiba, "imagictoken":imagictoken, "wow":wow}
		return render(request, "main/index.html", context )

@login_required(login_url='/signin')
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

@login_required(login_url='/signin')
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
@login_required(login_url='/signin')
def AllVettedView(request):
	vetted = Unvetted.objects.all().order_by('-pub_date')

	context = {	
		"vetted": vetted,
        }

	return render(request, "main/allvetted.html", context )

@login_required(login_url='/signin')
def VerifyVettedView(request, pk):
	vetted = Unvetted.objects.get(id=pk)

		

	context = {
        "vetted":vetted, 
        
    	}
	if request.method == "POST":
		vetted = Unvetted.objects.get(id=pk)
		vetted.status = True
		vetted.save()
			
		messages.success(request, 'updated')

	else:
		pass

	return render(request, 'main/verify_vetted.html', context)


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "welcome onboard "+user.username)
            current_user = request.user
            #userprofile = UserProfile.objects.get(user_id = current_user.id)
            #request.session['userimage'] = userprofile.image.url
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Error !! username or password is incorrect")
            return HttpResponseRedirect('/signin')
    current_user = request.user
    
    context = {
    }
    return render(request, 'main/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            user = authenticate(username=username, password=password)
            login(request, user)
            current_user = request.user
            #data = UserProfile()
            data.user_id = current_user.id

            data.image="images.png"
            data.save()
            messages.success(request, 'Account successfully created')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/signup')
    form = SignUpForm()

    context = {'form':form,  }
    return render(request, 'main/signup.html', context)

def logout_func(request):
    logout(request)
    messages.success(request, 'Logged out')
    return HttpResponseRedirect('/')
	