


from django.shortcuts import render 
from django.http import HttpResponseRedirect

from .models import *

from .forms import VenueForm, LiquidityForm, CollateralForm, CommitForm, BookingForm, Booking1Form, Booking2Form, Booking3Form, Booking4Form, Location1Form, Location2Form, Location3Form, Location4Form, Location5Form

# Create your views here.







def home(request):
	return render(request, 'co_servings/home.html')

def fbm(request):
	venue = Venue.objects.all()

	context = { 'value': venue}
	return render(request, 'co_servings/fbm.html', context)

	

def how(request):
	return render(request, 'co_servings/how.html')

def white(request):
	return render(request, 'co_servings/white.html')


def liquiditypools(request):
	liquidity = Liquidity.objects.all()
	
	starting = liquidity.count()
	filling_up = liquidity.filter(status='Filling_up').count()
	completed = liquidity.filter(status='Completed').count()
	
	context = {'topic': liquidity, 'starting':starting, 'filling_up':filling_up, 'completed':completed}
	return render(request, 'co_servings/liquiditypools.html', context )

def venue(request):
	submitted = False
	form = VenueForm()
	if request.method == "POST":
		form = VenueForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/venue?submitted=True')

	else:
		form = VenueForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/venue.html', {'form':form, 'submitted':submitted })




def projects(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/projects.html',context )

def liquidity(request):
	submitted = False
	form = LiquidityForm()
	if request.method == "POST":
		form = LiquidityForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/liquidity?submitted=True')

	else:
		form = LiquidityForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/liquidity.html', {'form':form, 'submitted':submitted })






def development(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()
	liquidity = Liquidity.objects.all()
	development = Development.objects.all()
	collaterals = Collateral.objects.all()
	


	context = {'list': projects, 'value': venue, 'list': collaterals,  'topic':liquidity}
	return render(request, 'co_servings/development.html',context )
	
	

def rental(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/rental.html',context )

	

def buildings(request):
	return render(request, 'co_servings/buildings.html')

def plan(request):
	return render(request, 'co_servings/plan.html')

def stand(request):
	return render(request, 'co_servings/stand.html')

def token(request):
	return render(request, 'co_servings/token.html')

def guest(request):
	return render(request, 'co_servings/guest.html')

def information1(request):
	return render(request, 'co_servings/information1.html')

def information2(request):
	return render(request, 'co_servings/information2.html')

def hostingrules(request):
	return render(request, 'co_servings/hostingrules.html')

def vaccineprotocol1(request):
	return render(request, 'co_servings/vaccineprotocol1.html')

def vaccineprotocol2(request):
	return render(request, 'co_servings/vaccineprotocol2.html')

def rentreduction(request):
	return render(request, 'co_servings/rentreduction.html')

def tokenprogram1(request):
	return render(request, 'co_servings/tokenprogram1.html')

def tokenprogram2(request):
	return render(request, 'co_servings/tokenprogram2.html')




def rentopportunity(request):

	projects = Project.objects.all()
	venue = Venue.objects.all()

	context = {'list': projects, 'value': venue}
	
	return render(request, 'co_servings/rentopportunity.html',context )







def ourcommunity1(request):
	return render(request, 'co_servings/ourcommunity1.html')

def ourcommunity2(request):
	return render(request, 'co_servings/ourcommunity2.html')

def development1(request):
	return render(request, 'co_servings/development1.html')

def overview1(request):
	return render(request, 'co_servings/overview1.html')

def overview2(request):
	return render(request, 'co_servings/overview2.html')

def guestrules(request):
	return render(request, 'co_servings/guestrules.html')

def costtrasparency(request):
	return render(request, 'co_servings/costtrasparency.html')

def guestopportunity(request):
	return render(request, 'co_servings/guestopportunity.html')

def reservation(request):
	return render(request, 'co_servings/reservation.html')

def payment1(request):
	return render(request, 'co_servings/payment1.html')

def payment2(request):
	return render(request, 'co_servings/payment2.html')

def trading(request):
	return render(request, 'co_servings/trading.html')

def investorsrules(request):
	return render(request, 'co_servings/investorsrules.html')

def tradingclarity(request):
	return render(request, 'co_servings/tradingclarity.html')

def tokenprogram3(request):
	return render(request, 'co_servings/tokenprogram3.html')

def tradingdesk(request):
	return render(request, 'co_servings/tradingdesk.html')

def ourcommunity3(request):
	return render(request, 'co_servings/ourcommunity3.html')

def report(request):
	return render(request, 'co_servings/report.html')

def news(request):

	return render(request, 'co_servings/news.html')

def owner(request):
	owner = Owner.objects.all()
	commit = Commit.objects.all()
	context = {'list': owner, 'value':commit }
	
	return render(request, 'co_servings/owner.html',context)



def gin(request):
	return render(request, 'co_servings/gin.html')

def pro(request):
	return render(request, 'co_servings/pro.html')

def ten(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()


	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/ten.html',context )
	



def sub(request):
	projects = Project.objects.all()
	venue = Venue.objects.all()


	context = {'list': projects, 'value': venue}
	return render(request, 'co_servings/sub.html',context)

def impressum(request):
	return render(request, 'co_servings/impressum.html')
def vigna(request):
	return render(request, 'co_servings/vigna.html')

def apts(request):
	return render(request, 'co_servings/apts.html')

	

def collateral(request):
	submitted = False
	form = CollateralForm()
	if request.method == "POST":
		form = CollateralForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/collateral?submitted=True')

	else:
		form = CollateralForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/collateral.html', {'form':form, 'submitted':submitted })



def gov(request):
	collaterals = Collateral.objects.all()
	

	context = {'list': collaterals }
	return render(request, 'co_servings/gov.html',context )

def commit(request):
	submitted = False
	form = CommitForm()
	if request.method == "POST":
		form = CommitForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/commit?submitted=True')

	else:
		form = CommitForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/commit.html', {'form':form, 'submitted':submitted })



def design1(request):
	bookings = Booking.objects.all()

	context = {'venue': bookings }
	return render(request, 'co_servings/design1.html',context)


def design2(request):
	booking1 = Booking1.objects.all()

	context = {'venue': booking1 }
	return render(request, 'co_servings/design2.html',context)
	
	

def design3(request):
	booking2 = Booking2.objects.all()
	

	context = {'venue': booking2 }
	return render(request, 'co_servings/design3.html',context)	
	

def design4(request):
	booking3 = Booking3.objects.all()

	context = {'venue': booking3 }
	return render(request, 'co_servings/design4.html',context)
	

def design5(request):
	booking4 = Booking4.objects.all()

	context = {'venue': booking4 }
	return render(request, 'co_servings/design5.html',context)
	


def booking(request):
	submitted = False
	form = BookingForm()
	if request.method == "POST":
		form = BookingForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking?submitted=True')

	else:
		form = BookingForm()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/booking.html', {'form':form, 'submitted':submitted })


def booking1(request):
	submitted = False
	form = Booking1Form()
	if request.method == "POST":
		form = Booking1Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking1?submitted=True')

	else:
		form = Booking1Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/booking1.html', {'form':form, 'submitted':submitted })

def booking2(request):
	submitted = False
	form = Booking2Form()
	if request.method == "POST":
		form = Booking2Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking2?submitted=True')

	else:
		form = Booking2Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/booking2.html', {'form':form, 'submitted':submitted })


def booking3(request):
	submitted = False
	form = Booking3Form()
	if request.method == "POST":
		form = Booking3Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking3?submitted=True')

	else:
		form = Booking3Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/booking3.html', {'form':form, 'submitted':submitted })

def booking4(request):
	submitted = False
	form = Booking4Form()
	if request.method == "POST":
		form = Booking4Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/booking4?submitted=True')

	else:
		form = Booking4Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/booking4.html', {'form':form, 'submitted':submitted })

def location1(request):
	submitted = False
	form = Location1Form()
	if request.method == "POST":
		form = Location1Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location1?submitted=True')

	else:
		form = Location1Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/location1.html', {'form':form, 'submitted':submitted })


def location2(request):
	submitted = False
	form = Location2Form()
	if request.method == "POST":
		form = Location2Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location2?submitted=True')

	else:
		form = Location2Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/location2.html', {'form':form, 'submitted':submitted })



def location3(request):
	submitted = False
	form = Location3Form()
	if request.method == "POST":
		form = Location3Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location3?submitted=True')

	else:
		form = Location3Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/location3.html', {'form':form, 'submitted':submitted })


def location4(request):
	submitted = False
	form = Location4Form()
	if request.method == "POST":
		form = Location4Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location4?submitted=True')

	else:
		form = Location4Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/location4.html', {'form':form, 'submitted':submitted })


def location5(request):
	submitted = False
	form = Location5Form()
	if request.method == "POST":
		form = Location5Form(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/location5?submitted=True')

	else:
		form = Location5Form()
		if 'submitted' in request.GET:
			submitted = True

		return render(request, 'co_servings/location5.html', {'form':form, 'submitted':submitted })


def news(request):
	location1s = Location1.objects.all()

	context = {'venue': location1s }
	return render(request, 'co_servings/news.html',context)

def news1(request):
	location2s = Location2.objects.all()

	context = {'venue': location2s }
	return render(request, 'co_servings/news1.html',context)

def news2(request):
	location3s = Location3.objects.all()

	context = {'venue': location3s }
	return render(request, 'co_servings/news2.html',context)

def news3(request):
	location4s = Location4.objects.all()

	context = {'venue': location4s }
	return render(request, 'co_servings/news3.html',context)

def news4(request):
	location5s = Location5.objects.all()

	context = {'venue': location5s }
	return render(request, 'co_servings/news4.html',context)



