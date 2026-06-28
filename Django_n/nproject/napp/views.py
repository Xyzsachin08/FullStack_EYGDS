from django.shortcuts import render
def index(request):
    return render(request,"napp/index.html")       

from .models import Contact
def Contact_list(request):
    Contacts=Contact.objects.all()
    return render(request,"contact.html",{'Contacts': Contacts})                                     
                                       
