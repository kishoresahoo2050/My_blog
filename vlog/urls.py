from django.urls import path
from . import views
urlpatterns = [
    path('', views.index,name="home"),
     path('About-Us', views.about,name="About"),
     path('Contact-Us',views.contact,name="Contact"),
     path('Signup',views.Signup,name="Signup"),
     path('Signin',views.Login,name="login"),
     path('Dashboard',views.Profile,name="profile"),


]