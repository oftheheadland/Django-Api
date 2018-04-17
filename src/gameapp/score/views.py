from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
import json
from score.models import Score
from django.views.decorators.csrf import csrf_exempt


# GET will expect an ID    localhost:8000/score/<id> and  return the score value
# POST will create a score of 0 for the specified ID



class HomePageView(APIView):

  
    @csrf_exempt
    def create_or_retrieve(self, request=None, userid = 0, format=None):
        if request.method == 'GET':
            try:
                found_score = Score.objects.get(id = userid)
                data = { "score": found_score.score, "id": id }
                return HttpResponse(json.dumps(data), status=200)

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchID"}), status=404)

        if request.method == "POST":
            try:
                found_user = Score.objects.get(id = userid)
                    
                u = Score(score=0)
                u.save()
                return HttpResponse(json.dumps({"status":"SuccessScoreSetToZero"}))

            except ObjectDoesNotExist as e:
                return HttpResponse(json.dumps({"status":"NoSuchUser3"}), status=404)
            

