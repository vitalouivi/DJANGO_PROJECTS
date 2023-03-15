from django.urls import path, re_path
from . import views


app_name = 'temp'
urlpatterns = [
    path('change_all/', views.change, name="change_all"),
    path('detail/<slug:slug>', views.TempDetail.as_view(), name="detail-temp"),
    path('detail/edit/<slug:slug>', views.edit, name="edit"),
    path('create/', views.TempCreateView.as_view(), name="create"),
    path('test/', views.testindex, name='test'),
    path('delete/<slug:slug>', views.create_Temp, name='delete'),
    path('update/<slug:slug>', views.create_Temp, name='update'),
    path('', views.TempListView.as_view(), name='index'),
    # create temp
    # update temp
    # delete temp

]