from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Mobile
from .forms import MobileForm

# CREATE + UPDATE
def mobile_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = MobileForm()
        else:
            mobile = get_object_or_404(Mobile, pk=id)
            form = MobileForm(instance=mobile)
        return render(request, "mobile_form.html", {"form": form})

    else:
        if id == 0:
            form = MobileForm(request.POST)
        else:
            mobile = get_object_or_404(Mobile, pk=id)
            form = MobileForm(request.POST, instance=mobile)

        if form.is_valid():
            form.save()

        return redirect('/list')


# READ
def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, "mobile_list.html", {"mobiles": mobiles})


# DELETE
def mobile_delete(request, id):
    mobile = get_object_or_404(Mobile, pk=id)
    mobile.delete()
    return redirect('/list')

