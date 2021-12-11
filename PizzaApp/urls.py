from django.urls import path


from . import views

app_name='PizzaApp'

urlpatterns = [
    path('',views.index, name='index'),
    path('topics',views.topics, name='topics'),
    path('topins',views.topins, name='topins'),
    path('topics/<int:topic_id>/',views.topic, name='topic'),
    path('topins/<int:topin_id>/',views.topin, name='topin'),
    path('new_topic',views.new_topic, name='new_topic'),
    path('new_topin',views.new_topin, name='new_topin'),
    path('new_entry/<int:topic_id>/',views.new_entry, name='new_entry'),
    path('new_entry1/<int:topin_id>/',views.new_entry1, name='new_entry1'),
    path('edit_entry/<int:entry_id>/',views.edit_entry, name='edit_entry'),
    path('edit_entry1/<int:entry1_id>/',views.edit_entry1, name='edit_entry1'),
    
    
]



