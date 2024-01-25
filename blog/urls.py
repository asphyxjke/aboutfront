from django.urls import path
from . import views
#Пути для url-маршрутизации приложения: все записи на главной страницы, конкретная запись по id и путь для добавления комментариев по id
urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments')]