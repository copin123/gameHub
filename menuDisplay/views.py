import re
from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import redirect
from menuDisplay.forms import LogMessageForm
from menuDisplay.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    model = LogMessage
    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data( **kwargs)
        return context
        
    

def about(request):
    return render(request, "menuDisplay/about.html")

def contact(request):
    return render(request, "menuDisplay/contact.html")

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid:
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
    else:
        return render(request, "menuDisplay/log_message.html", { "form": form })
    

def hello_there(request, name):
  return render(
      request,
      'menuDisplay/menuDisplay.html',
      {
          'name': name,
          'date': datetime.now()
      }
  )