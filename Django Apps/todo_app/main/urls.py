from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.homepage, name='home'),
    path('update/<str:task_name>/<str:task_id>',
         view=views.update_task, name='update'),
    path('delete/<str:task_name>/<str:task_id>',
         view=views.delete_task, name='delete'),
]
