import os 
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","PizzaProject.settings")

import django
django.setup()

from PizzaApp.models import Topic, Entry,Topin

topics= Topic.objects.all()


topins= Topin.objects.all()

for topic in topics:
    print(topic.id,topic)


t=Topic.objects.get(id=1)

print(t.text)

print(t.date_added)


entries=t.entry_set.all()


for topin in topins:
    print(topin.id,topin)


t=Topin.objects.get(id=1)




