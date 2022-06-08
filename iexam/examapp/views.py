from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from . import models, forms

def index(request):
    return render(request, 'index.html')

def registerPage(request):

	form = forms.CreateUserForm()
	if request.method == 'POST':
		form = forms.CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')


			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'register.html', context)


def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)
         
		if user is not None:
			login(request, user)
			return render(request, 'logout.html')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def BookUploadView(request):
    if request.method == 'POST':
        form = forms.UploadBookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = forms.UploadBookForm()
        context = {
            'form':form,
        }
    return render(request, 'UploadBook.html', context)

def viewbooks(request):
    books=models.EBooksModel.objects.all()
    return render(request,'viewbooks.html',{'books':books})