from user import views as uv
from score import views as sv
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().create_or_retrieve),
    path('user/<str:uname>/', uv.HomePageView().create_or_retrieve),

    path('score/', sv.HomePageView().get),
    path('score/<str:uname>/', sv.HomePageView().get),
]