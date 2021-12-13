from django.shortcuts import redirect, render
from .forms import EntryForm, TopicForm, TopinForm
from .models import Topic, Entry, Topin, Entry1
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, "PizzaApp/index.html")


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, "PizzaApp/topics.html", context)


def topins(request):
    topins = Topin.objects.order_by('date_added')
    context = {'topins': topins}
    return render(request, "PizzaApp/topins.html", context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.all()
    context = {"topic": topic, 'entries': entries}
    return render(request, "PizzaApp/topic.html", context)


def topin(request, topin_id):
    topin = Topin.objects.get(pk=topin_id)
    entries = [topin]
    context = {"topin": topin, 'entries': entries}
    return render(request, "PizzaApp/topin.html", context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('PizzaApp:topics')

    context = {'form': form}
    return render(request, "PizzaApp/new_topic.html", context)


@login_required
def new_topin(request):
    if request.method != 'POST':
        form = TopinForm()
    else:
        form = TopinForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('PizzaApp:topins')

    context = {'form': form}
    return render(request, "PizzaApp/new_topin.html", context)


@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('PizzaApp:topic', topic_id=topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, "PizzaApp/new_entry.html", context)


@login_required
def new_entry1(request, topin_id):
    topin = Topin.objects.get(id=topin_id)
    if request.method != 'POST':
        form = EntryForm
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid:
            new_entry1 = form.save(commit=False)
            new_entry1.topin = topin
            new_entry1.save()
            return redirect('PizzaApp:topin', topin_id=topin_id)

    context = {'form': form, 'topin': topin}
    return render(request, "PizzaApp/new_entry1.html", context)


@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('PizzaApp:topic', entry_id=entry_id)

    context = {'entry': entry, 'form': form, 'topic': topic}
    return render(request, "PizzaApp/edit_entry.html", context)


@login_required
def edit_entry1(request, entry1_id):
    entry1 = Entry1.objects.get(id=entry1_id)
    topin = entry1.topin

    if request.method != 'POST':
        form = EntryForm(instance=entry1)
    else:
        form = EntryForm(instance=entry1, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('PizzaApp:topin', entry1_id=entry1_id)

    context = {'entry1': entry1, 'form': form, 'topin': topin}
    return render(request, "PizzaApp/edit_entry1.html", context)


def logged_out(request):
    return render(request, "PizzaApp/index.html")
