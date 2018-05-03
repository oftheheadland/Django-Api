
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from subscribe.models import Subscribe
from django.views.decorators.csrf import csrf_exempt



class HomePageView(APIView):



    @csrf_exempt
    def create_or_retrieve(self, request=None, userid = 0, format=None):
        if request.method == 'GET':
            try:
                found_subscribe = Subscribe.objects.get(id = userid)
                data = { "subscribe": found_subscribe.level, "id": userid }
                return HttpResponse(json.dumps(data), status=200)

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchID"}), status=404)

        if request.method == "POST":
            try:
                found_user = Subscribe.objects.get(id = userid)
                return HttpResponse(json.dumps({"status":"AlreadyExists"}), status=403)

            except ObjectDoesNotExist as e:
                pass

            s = Subscribe(level=0)
            s.save()
            return HttpResponse(json.dumps({"status":"SuccessScoreSetToZero"}))
