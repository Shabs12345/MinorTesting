from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserForms, Contact
from .models import Users
from django.contrib import messages

# Create your views here.
def base(request):
    if request.method == "POST":
        form = Contact(request.POST)
        context = {
            'forms': form,
            'error': 1
        }
        if form.is_valid():
            print form.cleaned_data['name']
        else:
            print "Invalid"
        return HttpResponseRedirect('/project/index')
    else:
        form = Contact()
        context = {
            'forms': form,
            'title': "Contact",
            'error': 0,
        }
    return render(request, "base.html", context)


def index(request):
    return render(request, "index.html", {})


def login(request):
    if request.method == 'POST':
        form = UserForms(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email_id']
            password = form.cleaned_data['password']
            try:
                userobj = Users.objects.get(email_id=email, password=password)
            except Exception:
                msg = "Invalid Email ID / Password"
                messages.add_message(request, messages.INFO, msg)
                return HttpResponseRedirect('login')
            name = userobj.first_name
            msg = 'Welcome To Django'
            messages.add_message(request, messages.INFO, msg)
            messages.add_message(request, messages.INFO, name)
            return HttpResponseRedirect("index")
        else:
            if form.errors.keys()[0] == 'email_id':
                msg = "Enter the Email ID Field"
            elif form.errors.keys()[0] == 'password':
                msg = "Enter the Password Field"
            messages.add_message(request, messages.INFO, msg)
            return HttpResponseRedirect('login')
    else:
        form = UserForms()
        context = {
            "forms": form,
            "title": "login",
            "error": 0,
            "msg": "Unknown",
        }
    return render(request, "login.html", context)
