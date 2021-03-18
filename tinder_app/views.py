from django.shortcuts import render, redirect
from . models import *
from . forms import *
from django.http import HttpResponseRedirect



def home(request):
	dogs = Dog.objects.all()

	context = {'dogs':dogs}
	return render(request, 'tinder_app/home.html', context)



def details(request, pk):
	dogs_details = Dog.objects.filter(pk=pk)

	context = {'dogs_details':dogs_details}
	return render(request, 'tinder_app/details.html', context)



def edit(request, pk):
	dogs = Dog.objects.get(pk=pk)
	form = DogForm(instance=dogs)

	if request.method == 'POST':
		form = DogForm(request.POST, instance=dogs)
		if form.is_valid():
			form.save()
			return redirect('home')

	context = {'dogs':dogs, 'form':form}
	return render(request, 'tinder_app/edit.html', context)



def delete(request, pk):
	dogs = Dog.objects.get(pk=pk)
	dogs_info = Dog.objects.filter(pk=pk)

	if request.method == 'POST':
		dogs.delete()
		return redirect('home')

	context = {'dogs':dogs, 'dogs_info':dogs_info}
	return render(request, 'tinder_app/delete.html', context)



def create(request):
	dogs = Dog.objects.all()
	form = DogForm()

	created = False

	if request.method == 'POST':
		form = DogForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/create?created=True')

	else:
		form = DogForm()
		if 'created' in request.GET:
			created = True

	context = {'dogs':dogs, 'form':form, 'created':created}
	return render(request, 'tinder_app/create.html', context)



def search(request):
	if request.method == 'POST':
		search = request.POST['search']
		dogs = Dog.objects.filter(breed__breed__icontains=search)

		context = {'search':search, 'dogs':dogs}
		return render(request, 'tinder_app/search.html', context)

	else:
		return render(request, 'tinder_app/search.html')