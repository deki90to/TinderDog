from django import forms
from . models import DogBreed, Dog


class DogForm(forms.ModelForm):
	class Meta:
		model = Dog
		fields = '__all__'

		labels = {
		'breed':'Rasa',
		'gender':'',
		'birthYear':'',
		'info':'',
		'phone_no':'',
		'date':'' ,
		'image':'',
		'image2':'',
		'image3':'',
		'image4':'',
		'image5':'',
		'image6':'',
		}

		widgets = {
			'user':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'admin', 'type':'hidden'}),
			'gender':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Pol'}),
			'birthYear':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Godina Rodjenja'}),
			'info':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vise Informacija'}),
			'phone_no':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Broj Telefona'}),
			'date':forms.TextInput(attrs={'class':'form-control'}),
		}