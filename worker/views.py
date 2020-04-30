from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Worker
from django.core.serializers import serialize
from .mixins import *
from django.views.generic import View
## JsonResponse ==> Userd to convert dict into json using dajngo jsonResponse function
import json
# Create your views here.

class WorkerDetailCBV(SerializeMixin, HttpResponseMixin, View):

    def get(self, request, id, *args,**kwargs):
        try:
            print("id==",id)
            worker = Worker.objects.get(id=id)
        except Worker.DoesNotExist:
            json_data = json.dumps({"msg":"requested resource is not available"})
            return self.rende_to_http_response(json_data)
        else:
            json_data = self.serialize([worker,])
            return self.rende_to_http_response(json_data)

class WorkerListCBV(SerializeMixin, HttpResponseMixin, View):

     def get(self, request, *args,**kwargs):
         try:
             workers = Worker.objects.all()
             json_data = self.serialize(workers)
         except  Worker.DoesNotExist:
             json_data = json.dumps({"msg": "requested resource is not available"})
             return self.rende_to_http_response(json_data)
         else:
             return self.rende_to_http_response(json_data)

     def post(self, request, *args,**kwargs):
        json_data = json.dumps({"msg": "post request is get called"})
        return self.rende_to_http_response(json_data)





