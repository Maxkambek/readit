from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Contact
from .forms import CreateContactForm


def contact_view(request):

    form=CreateContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.succes(request,'succesfully send')
        return redirect('.')
    context={
        'form':form
    }
    return render(request,'contact/index.html',context)