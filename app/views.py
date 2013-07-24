from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.utils import simplejson
from django import forms
#from django.contrib.auth.decorators import login_required

import pdb_api

db = pdb_api.pdb()

@csrf_exempt
def index(request):
	if request.method == "POST":
		first_name = request.POST['firstName']
		try:
			middle = request.POST['middleInitial']
		except:
			middle = "NULL"
		last_name = request.POST['lastName']
		location = request.POST['location']
		team = request.POST['teamName']
		pemail = request.POST['personalEmail']
		try:
			nda = request.POST['nda']
			if nda == 'Yes': nda = 1
		except:
			nda = 0
		try:
			early = request.POST['earlyAccess']
			if early == 'Yes': early = 1
		except:
			early = 0

		success = db.insert_user(first_name, last_name, middle, location, team, pemail, early, nda)
		return render_to_response('index.html', {})
	else:
		return render_to_response('index.html', {})

def list(request):
        return render_to_response('list.html', {})

def api_list(request):
	user_list = db.get_user_list()
	return render_to_response('list.html', {'users': user_list})

@csrf_exempt
def api_process(request):
	user_list = db.get_user_list()
	if request.method == "POST":
		ids = []
		for field in request.POST.iterkeys():
			if field.count('user-') > 0:
				ids.append(request.POST[field])
		success = db.insert_job_start(ids)
		return render_to_response('process.html', {'users': user_list})
	return render_to_response('process.html', {'users': user_list})

def api_process_update(request):
	process_list = db.get_user_que()
	return HttpResponse(simplejson.dumps(process_list), mimetype='application/json')

@csrf_exempt
def process(request):
        return render_to_response('process.html', {})

