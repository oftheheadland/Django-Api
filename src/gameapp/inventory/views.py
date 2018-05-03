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
            try:
                found_desc = Inventory.objects.get(description=objdescription)
                data = { "description": objdescription,  "id": found_desc.id}
                return HttpResponse(json.dumps(data), status=200)

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchID"}), status=404)


        elif request.method == "POST":
            try:
                found_description = Inventory.objects.get(description=objdescription)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            
            except ObjectDoesNotExist as e:
                pass

            u = Inventory(description=objdescription)
            u.save()
            return HttpResponse(json.dumps({"status":"SuccessSetDescription"}))


