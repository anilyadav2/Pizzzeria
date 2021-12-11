import os 
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE","PizzaProject.settings")

import django
django.setup()

from PizzaApp.models import Topic, Entry

topics= Topic.objects.all()


for topic in topics:
    print(topic.id,topic)


t=Topic.objects.get(id=1)

print(t.text)

print(t.date_added)


entries=t.entry_set.all()
