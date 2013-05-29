from django.conf.urls import patterns, include, url


from gamehub import views



urlpatterns = patterns ('',


	# Blank after gamehub/ so this will be index page
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='gamedetail'),

)