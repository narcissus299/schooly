from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.contrib.auth.models import User
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from schooly_app.forms import *
from schooly_app.models import *

#TODO : Templates not working -fucking Templates- 
#the most basic thing I need to have a fucking UI
#Oh god what am I doing with my life
#FML I should burn this and go to sleep

def index(request,auth_form=None,user_form=None):
	if not request.user.is_authenticated():
		auth_form = auth_form or AuthenticateForm()
		user_form = user_form or UserCreateForm()

		return render(request,'landing.html',{'auth_form': auth_form, 'user_form': user_form, })

	else:

		'''Display all classes signed up for by the user'''
		classes = request.user.id.class_participants.all()
		dic = dict( (i.name,i.code) for i in classes )

		return render(request, 'classes.html', dic)


def class_view(request, classid):
	pass

def create_class(request):
	pass

def join_class(request):
	pass

def login_view(request):
	if request.method == 'POST':
		form = AuthenticateForm(data=request.POST)
		if form.is_valid():
			login(request, form.get_user())
			# Success
			return redirect('/')
		else:
			# Failure
			return index(request, auth_form=form)
	return redirect('/')
 
 
def logout_view(request):
	logout(request)
	return redirect('/')

def signup(request):
	user_form = UserCreateForm(data=request.POST)
	if request.method == 'POST':
		if user_form.is_valid():
			username = user_form.clean_username()
			password = user_form.clean_password2()
			user_form.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('/')
		else:
			return index(request, user_form=user_form)
	return redirect('/')