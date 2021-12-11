from django.shortcuts import redirect, render
from.forms import EntryForm, TopicForm
from .models import Topic, Entry
# Create your views here.

def index(request):
    return render(request,"PizzaApp/index.html")


def topics(request):
    topics= Topic.objects.order_by('date_added')
    context={'topics':topics}
    return render(request,"PizzaApp/topics.html",context)



def topic(request,topic_id):
    topic= Topic.objects.get(id=topic_id)
    entries=topic.entry_set.all()
    context={"topic":topic,'entries':entries}
    return render(request,"PizzaApp/topic.html",context)


def new_topic(request):
    if request.method != 'POST':
        form=TopicForm()
    else:
        form= TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('PizzaApp:topics')

    context={'form':form}
    return render(request,"PizzaApp/new_topic.html",context)


def new_entry(request,topic_id):
    topic= Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form= EntryForm
    else:
        form=EntryForm(data=request.POST)
        if form.is_valid:
            new_entry=form.save(commit=False)
            new_entry.topic= topic
            new_entry.save()
            return redirect('PizzaApp:topic',topic_id=topic_id)

    context={'form':form, 'topic':topic}
    return render(request,"PizzaApp/new_entry.html",context)




def edit_entry(request,entry_id):
    entry= Entry.objects.get(id=entry_id)
    topic = entry.topic


    if request.method != 'POST':
        form= EntryForm(instance=entry)
    else:
        form=EntryForm(instance=entry,data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('PizzaApp:topic',entry_id=entry_id)

    context={'entry':entry,'form':form, 'topic':topic}
    return render(request,"PizzaApp/edit_entry.html",context)




def logged_out(request):
    return render(request,"PizzaApp/index.html")



