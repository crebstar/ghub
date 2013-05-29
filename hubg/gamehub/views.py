# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import Context, loader
from django.shortcuts import render, get_object_or_404 # 404 is Http response for not found
from django.views import generic
from django.utils import timezone

from gamehub.models import *

class IndexView(generic.ListView):
	template_name = 'gamehub/index.html'
	model = Game


	def get_context_data(self, **kwargs):
		# kw args allows for key/value pairs of data to be passed in a function and then
		# wrapped into a single dictionary variable called kwargs	
		context = super(IndexView, self).get_context_data(**kwargs)
		context['curTime'] = timezone.now()
		context['dev'] = 'Crebstar'
		context['title'] = 'Game List'
		context['games'] = Game.objects.all()
		return context;


class GameDetailView(generic.DetailView):
	template_name = 'gamehub/gamedetail.html'
	model = Game

	# I think ideally I should be narrowing the result set in 
	# the get_queryset function

	def get_context_data(self, **kwargs):
		context = super(GameDetailView, self).get_context_data(**kwargs)

		#  This is most likely terrible practice
		#  tomorrow lookup how to do overriding of get_queryset
		#  This doesn't throw a 404 
		context['gameSelected'] = Game.objects.get(pk=int(self.kwargs['pk']))
		context['gameDescription'] = context['gameSelected'].gamedescription_set.get(pk=int(self.kwargs['pk']))

		return context


	
