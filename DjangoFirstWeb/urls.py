from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("submit/",views.signup,name="submit"),
    path("welcome/",views.welcome,name="welcome"),
    path("<int:id>/delete",views.deletetodo,name="deletetodo")   
]