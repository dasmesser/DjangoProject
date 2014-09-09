from django.conf.urls import patterns, url
from charts import views

urlpatterns = patterns('',
	url(r'^fecha/$', views.fecha, name='fecha'),
	url(r'^delegaciones/$', views.delegaciones, name='delegaciones'),
	url(r'^delegacion/(?P<delegacion>\w+)/$', views.delegacion, name='delegacion'),
	url(r'^juzgado/(?P<delegacion>\w+)/(?P<juzgado>\d+)$', views.juzgado, name='juzgado'),
)