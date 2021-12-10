
from django.shortcuts import redirect, render
#from .forms import EntryForm, TopicForm
from .models import Pizza_name
# Create your views here.

def index(request):
    return render(request,"PizzaApp/index.html")


