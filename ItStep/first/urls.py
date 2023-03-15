from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('accounts/login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    path('accounts/password_change', PasswordChangeView.as_view(template_name='user/change_password.html'),
         name='password_change'),
    path('accounts/password_change/done', PasswordChangeDoneView.as_view(template_name='user/changed_password.html'),
         name='password_change_done'),


    path('accounts/password_reset/', PasswordResetView.as_view(template_name='user/reset.html',
                                                               subject_template_name='emails/header.txt',
                                                               email_template_name='emails/body.txt'),
         name='reset_password'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(template_name='user/reset_sent.html'),
         name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='user/reset_form.html'),
         name='password_reset_confirm'),
    path('accounts/reset/done', PasswordResetCompleteView.as_view(template_name='user/reset_done.html'),
         name='password_reset_complete'),


    path('', include('main.urls')),
    #path('bboard/', include('main.urls', namespace='new-bboard')),
    path('users/', include('user.urls')),
    path('templates/', include('temp_app.urls')),
    path('admin/', admin.site.urls),
]

