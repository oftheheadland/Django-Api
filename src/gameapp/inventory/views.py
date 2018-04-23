from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from inventory.models import Inventory
from django.views.decorators.csrf import csrf_exempt

class HomePageView(APIView):
	
    @csrf_exempt
    def create_or_retrieve(self, request=None, objdescription="test", format=None):
        if request.method == 'GET':

            found_description = Inventory.objects.get(description=objdescription)
            if(found_description):
                return HttpResponse(json.dumps(data), status=200)
            else:
                return HttpResponse(json.dumps({"status":"NoSuchDescription"}), status=404)

        elif request.method == "POST":
            try:
                found_description = Inventory.objects.get(description=objdescription)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = Inventory(description=objdescription)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))

    def get(self, request=None, objdescription="test", format=None):
        try:
            found_description = Inventory.objects.get(description=objdescription)
        except ObjectDoesNotExist as e:
            return HttpResponse(json.dumps({"status":"NoSuchDescription"}), status=404)

        data = { "inventory": objdescription, "id": found_description.id }
        return HttpResponse(json.dumps(data))