from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),

    # Urls for diary
    path('diary/', views.diaryPage, name = 'view_diary'),
    path('diary/new', views.newDiary, name = 'newDiary'),
    path('diary/del/<int:id>', views.delDiary, name = 'del_diary'),
    path('diary/edit/<int:id>', views.editDiary, name = 'edit_diary'),

    #Urls for todo_list
    path('tasks/', views.taskPage, name = 'view_tasks'),
    path('tasks/new', views.newTask, name = 'new_task'),
    path('tasks/del/<int:id>', views.delTask, name = 'del_task'),
    path('tasks/edit/<int:id>', views.editTask, name='edit_task'),
]