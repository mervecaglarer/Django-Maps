"""fusioncharts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from samples import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""
from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from fusioncharts.views import catalogue
from fusioncharts import datahandler
from fusioncharts.samples import rendering_map_using_dictionary_example
from fusioncharts.samples import  rendering_map_using_json_example

urlpatterns = [
    url(r'^$', catalogue),
    url(r'^admin/', admin.site.urls),
    url(r'^datahandler', datahandler.getdata),
    url(r'^rendering-map-using-dictionary-example', rendering_map_using_dictionary_example.chart, name='chart'),
    url(r'^rendering-map-using-json-example', rendering_map_using_json_example.chart, name='chart'),
]