from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
def index(request):
    context = {
  "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
  }
    return render(request, 'time_of_day/index.html', context)

def time_display(request):
    return redirect('/')


# Create your views here.
