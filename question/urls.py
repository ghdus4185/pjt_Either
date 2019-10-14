from django.urls import path, include
from . import views
app_name = 'question'
urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('<int:id>/', views.detail, name="detail"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('<int:id>/update1/', views.update1, name="update1"),
    path('<int:id>/update2/', views.update2, name="update2"),

    path('<int:id>/edit/', views.edit, name="edit"),

    path('<int:question_id>/answers/', views.answer_create, name="answer_create"),
    path('<int:question_id>/answers/<int:answer_id>/delete', views.answer_delete, name="answer_delete"),

    path('random/', views.random, name="random"),

    path('search/', views.search, name="search")

]
