from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('add/',views.addTodo, name='add'),
    path('complete/<todo_id>',views.completeTodo, name='complete'),
    path('deliteall',views.delete_completed, name='delite_completed'),
    path('delite',views.delete_all, name='delete_all'),

]
