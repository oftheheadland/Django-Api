from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from user.models import User
from django.views.decorators.csrf import csrf_exempt

class HomePageView(APIView):

    @csrf_exempt
    def create_or_retrieve(self, request=None, uname="test", format=None):
        if request.method == 'GET':

            found_user = User.objects.get(name=uname)
            if(found_user):
                return HttpResponse(json.dumps(data), status=200)
            else:
                return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        elif request.method == "POST":
            try:
                found_user = User.objects.get(name=uname)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)
            except ObjectDoesNotExist as e:
                pass
            u = User(name=uname)
            u.save()
            return HttpResponse(json.dumps({"status":"Success"}))

    def get(self, request=None, uname="test", format=None):
        try:
            found_user = User.objects.get(name=uname)
        except ObjectDoesNotExist as e:
            return HttpResponse(json.dumps({"status":"NoSuchUser"}), status=404)

        data = { "user": uname, "id": found_user.id }
        return HttpResponse(json.dumps(data))