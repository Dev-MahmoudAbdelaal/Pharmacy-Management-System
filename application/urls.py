from django.urls import path
from . import views
app_name ='application'
urlpatterns = [
    path("Home",views.Home , name = 'Home') ,
    path("signup",views.signup , name = 'signup') ,
    path("update",views.update , name = 'update') ,
    path("delete/<id>", views.deletewithid, name="deletewithid"),
    path("update/<id>", views.update, name="update"),
    
 ]