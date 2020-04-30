from django.contrib import admin
from .models import Worker
# Register your models here.
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['wid', 'wfirstname', 'wlastname']

admin.site.register(Worker, WorkerAdmin)
