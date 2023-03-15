from django.urls import path, re_path
from . import views


app_name = 'user'
urlpatterns = [
    path('user-<slug:slug>/', views.UserDetailView.as_view(), name='user-info'),
    path('new-user/', views.UserAddView.as_view(), name='new-user'),
    path('', views.UserListView.as_view(), name='index'),
]