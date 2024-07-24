from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.dashboard,name='dashboard'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
     path('logout/', views.custom_logout, name='logout'),
    path('password-change/',auth_views.PasswordChangeView.as_view(),name='password-change'),
    path('password-change-done/',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('profile/', views.user_profile, name='user-profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(),name='password-reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password-reset-confirm'),
    path('reset/done',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('register/',views.register, name='register')
]  