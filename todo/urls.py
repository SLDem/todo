from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('add_item/', views.add_item, name='add_item'),
    path('complete_task/<int:pk>', views.complete_task, name='complete_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task')
]
