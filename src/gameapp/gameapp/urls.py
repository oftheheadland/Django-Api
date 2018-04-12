from user import views as uv
from django.urls import path

urlpatterns = [
    path('user/', uv.HomePageView().get),
    path('user/<str:uname>/', uv.HomePageView().get),
]