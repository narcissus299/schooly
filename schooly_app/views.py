from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from schooly_app.forms import *
from schooly_app.models import *

def index(request):
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
	pass

def logout_view(request):
	pass

def signup(request):
	pass