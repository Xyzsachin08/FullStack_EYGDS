from django.urls import path 
from.import views
urlpatterns = [
    path(" ",views.index,name="index"),
]   
from.views import Contact_list
urlpatterns=[
    path(" ",views.index,name="index"),
    path("contacts/", Contact_list,name= "Contacts"),
]
