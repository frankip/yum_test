# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
import datetime
from django.http import HttpResponse
from django.contrib import admin
from .models import Details
# Register your models here.


def export_to_csv(modeladmin, request, queryset):
	opts = modeladmin.model._meta
	response = HttpResponse(content_type= 'text/csv')
	response['Content-Disposition'] = 'attachment;\
		filename={}.csv'.format(opts.verbose_name)
	writer = csv.writer(response)

	fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
	# write first row with header information
	writer.writerow([field.verbose_name for field in fields])
	# write data rows
	for obj in queryset:
			data_row = []
			for field in fields:
				value = getattr(obj, field.name)
				if isinstance(value, datetime.datetime):
					value = value.strftime('%d/%m/%y')
				data_row.append(value)
			writer.writerow(data_row)
			return response
	export_to_csv.short_description = 'Export to CSV'


class FeedformAdmin(admin.ModelAdmin):
	list_display = [
		'user',
		'phone_number', 
		'neighbourhood', 
		'rating',
		'comments'
		]
	actions = [export_to_csv]

admin.site.register (Details,FeedformAdmin)