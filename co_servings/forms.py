from django import forms
from django.forms import ModelForm
from .models import Venue, Liquidity, Collateral, Commit, Booking 


class VenueForm(ModelForm):
	class Meta:
		model = Venue
		fields = ('owner', 'property_price', 'location',  'category', 'building', 'total_project_price', 'temp')

		widgets = {
			'owner': forms.TextInput(attrs={'class':'form-control'}),
			'property_price': forms.TextInput(attrs={'class':'form-control'}),
			
			
			'location': forms.TextInput(attrs={'class':'form-control'}),
			
			'building': forms.TextInput(attrs={'class':'form-control'}),
			
			'total_project_price': forms.TextInput(attrs={'class':'form-control'}),
			'temp': forms.TextInput(attrs={'class':'form-control'}),
			
			}	
		
		labels = {
            'owner': 'Owner : example Joe Doe, etc..',
           
            'property_price': 'Property_Price : example € 2.500.000, etc...',
          
            'location': 'Location : example 1.1-milan/1, 2-berlin/1, etc...',
            'building': 'Building : example fbm-2, fbm-3, etc... from Meta-Catalogue in main menu',
            'total_project_price': 'Total_Project_coast: example € 7.500.000, etc...',
            'temp': 'Temp: example  fom-1, fom-2, etc... from Meta-Catalogue in main menu',
           
            }

class LiquidityForm(ModelForm):
	class Meta:
		model = Liquidity
		fields = ('topic', 'name', 'price', 'status')

		widgets = {
			'topic': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'price': forms.TextInput(attrs={'class':'form-control'}),
			
			
			
		}	

		labels = {
            'topic': 'Type : example Private Investor, Private Fund, etc..',
            
            'name': 'Liquidty Pool : example ETH/TIPI',
            'price': 'Value: € 15.000.000',
          }

class CollateralForm(ModelForm):
	class Meta:
		model = Collateral
		fields = ('state', 'city', 'ministry', 'pool', 'amount')

		widgets = {
			'state': forms.TextInput(attrs={'class':'form-control'}),
			'city': forms.TextInput(attrs={'class':'form-control'}),
			'ministry': forms.TextInput(attrs={'class':'form-control'}),
			
			'pool': forms.TextInput(attrs={'class':'form-control'}),
			'amount': forms.TextInput(attrs={'class':'form-control'}),
			
			}

		labels = {
            'state': 'State : example 1-ITALY, 2-GERMANY, 3-FRANCE, 4-USA',
           
            'city': 'City : example milan, berlin, etc...',
          
            'ministry': 'Ministry : example infrastructure, housing, etc...',
            'pool': 'Pool : ETH/TIPI',
            'amount': 'Amount  € 15.000.000',
           
            }	
		

class CommitForm(ModelForm):
	class Meta:
		model = Commit
		fields = ('location', 'agreement_govern', 'agreement_investor', 'agreement_property_owner', 'agreement_tenant', 'agreement_guest')

		widgets = {
			'location': forms.TextInput(attrs={'class':'form-control'}),
			'agreement_govern': forms.TextInput(attrs={'class':'form-control'}),
			'agreement_investor': forms.TextInput(attrs={'class':'form-control'}),
			'agreement_property_owner': forms.TextInput(attrs={'class':'form-control'}),
			'agreement_tenant': forms.TextInput(attrs={'class':'form-control'}),
			'agreement_guest': forms.TextInput(attrs={'class':'form-control'}),
			
			

		}	

		
		 

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ('project', 'name', 'building', 'duplex', 'number', 'starting', 'email', 'phone' )

		widgets = {
			'project': forms.TextInput(attrs={'class':'form-control'}),
			'name': forms.TextInput(attrs={'class':'form-control'}),
			'building': forms.TextInput(attrs={'class':'form-control'}),
			'duplex': forms.TextInput(attrs={'class':'form-control'}),
			'number': forms.TextInput(attrs={'class':'form-control'}),
			'starting': forms.TextInput(attrs={'class':'form-control'}),
			'email': forms.TextInput(attrs={'class':'form-control'}),
			'phone': forms.TextInput(attrs={'class':'form-control'}),

		}

		labels = {
            'project': 'Project : example 1-milan/1, 2-berlin/1, etc..',
            'email': 'my_email',
            'building': 'Building : example fbm-2, fbm-3, etc...',
            'name': 'Name: example Joe Doe, etc...',
            'duplex': 'Duplex : example A, B, etc...',
            'number': 'Number : example 1, 2, etc...',
            'starting': 'Starting Rental dd/mm/yy',
            'phone': 'my_phone',
        }
