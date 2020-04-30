from django.core.serializers import serialize
import json

from django.http import HttpResponse

class SerializeMixin(object):

    def serialize(self, qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_data = []
        for data in p_data:
            final_data.append(data.get('fields',[]))
        final_data = json.dumps(final_data)
        return final_data

class HttpResponseMixin(object):

    def rende_to_http_response(self, json, status=200):
        return HttpResponse(json, content_type='application/json', status=status)

