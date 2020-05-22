from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'homepage'),

    # Urls for diary
    path('diary/', views.diaryPage, name = 'view_diary'),
    path('diary/new', views.newDiary, name = 'newDiary'),
    path('diary/del/<int:id>', views.delDiary, name = 'del_diary'),
    path('diary/edit/<int:id>', views.editDiary, name = 'edit_diary'),
]