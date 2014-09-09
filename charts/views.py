from django.shortcuts import render
from django.http import HttpResponse
from tools import data_reader

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as ticker
# Create your views here.

#url(r'^$', views.fecha, name='fecha'),
#url(r'^(?P<delegacion>\d+)/$', views.delegacion, name='delegacion'),
#url(r'^(?P<delegacion>\d+)/(?P<juzgado>\d+)/$', views.juzgado, name='juzgado'),

def fecha(request):
	res = data_reader.read_file_fecha()
	sorted_data = sorted(res.items(), data_reader.date_compare)
	
	chart_data = np.array(sorted_data, dtype=[('fecha', list),('matrimonios', int)])
	chart_data = chart_data.view(np.recarray)
	
	l = len(chart_data)
	
	def formater(x, pos=None):
		if l <= x:
			return chart_data.fecha[l-1]
		else:
			return chart_data.fecha[x]
	
	response = HttpResponse(content_type='image/png')
	fig, ax = plt.subplots()
	ax.plot(np.arange(l), chart_data.matrimonios, 'o-')
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(formater))
	fig.autofmt_xdate()
	
	plt.title('Grafica acumulativa del numero de matrimonios en el DF por fecha')
	plt.xlabel('Fecha')
	plt.ylabel('Numero de casamientos')
	
	plt.savefig(response, format='png')
	return response
	
def delegaciones(request):
	res = data_reader.read_file_delegaciones()
	sorted_data = sorted(res.items())
	
	chart_data = np.array(sorted_data, dtype=[('delegacion', list),('matrimonios', int)])
	chart_data = chart_data.view(np.recarray)
	
	l = len(chart_data)
	
	def formater(x, pos=None):
		if l <= x:
			return chart_data.delegacion[l-1]
		else:
			return chart_data.delegacion[x]
	
	response = HttpResponse(content_type='image/png')
	fig, ax = plt.subplots()
	ax.plot(np.arange(l), chart_data.matrimonios, 'o-')
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(formater))
	fig.autofmt_xdate(.4, 45)
	
	plt.title('Numero de matrimonios en el DF por delegacion')
	plt.xlabel('Delegacion')
	plt.ylabel('Numero de casamientos')
	
	plt.savefig(response, format='png')
	return response

def delegacion(request, delegacion):
	(res, del_real) = data_reader.read_file_delegacion(delegacion)
	
	if len(res) == 0:
		return HttpResponse('No existe tal delegacion')
	
	sorted_data = sorted(res.items(), data_reader.juzgado_compare)
	
	chart_data = np.array(sorted_data, dtype=[('juzgado', list),('matrimonios', int)])
	chart_data = chart_data.view(np.recarray)
	
	l = len(chart_data)
	
	def formater(x, pos=None):
		if l <= x:
			return chart_data.juzgado[l-1]
		else:
			return chart_data.juzgado[x]
	
	response = HttpResponse(content_type='image/png')
	fig, ax = plt.subplots()
	ax.plot(np.arange(l), chart_data.matrimonios, 'o-')
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(formater))
	
	plt.title('Numero de matrimonios en el DF, delegacion ' + del_real + ' por juzgado')
	plt.xlabel('Juzgado')
	plt.ylabel('Numero de casamientos')
	
	plt.savefig(response, format='png')
	return response
	
def juzgado(request, delegacion, juzgado):
	(res, del_real) = data_reader.read_file_juzgado(delegacion, juzgado)
	
	if len(res) == 0:
		return HttpResponse('No existe tal delegacion')
	
	sorted_data = sorted(res.items(), data_reader.date_compare)
	
	chart_data = np.array(sorted_data, dtype=[('fecha', list),('matrimonios', int)])
	chart_data = chart_data.view(np.recarray)
	
	l = len(chart_data)
	
	def formater(x, pos=None):
		if l <= x:
			return chart_data.fecha[l-1]
		else:
			return chart_data.fecha[x]
	
	response = HttpResponse(content_type='image/png')
	fig, ax = plt.subplots()
	ax.plot(np.arange(l), chart_data.matrimonios, 'o-')
	ax.xaxis.set_major_formatter(ticker.FuncFormatter(formater))
	
	plt.title('Numero de matrimonios en el DF, delegacion ' + del_real + ' en el juzgado ' + juzgado)
	plt.xlabel('Fecha')
	plt.ylabel('Numero de casamientos')
	
	plt.savefig(response, format='png')
	return response
	
	