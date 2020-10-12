from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name='homepage'),
    path('register_schooladmin/', views.register_schooladmin, name='register_schooladmin'),
    path('register_student/', views.register_student, name='register_student'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('send_notes/', views.send_notes, name='send_notes'),
    path('see_notes/', views.see_notes, name='see_notes'),
    path('admin_show_notes/', views.admin_show_notes, name='admin_show_notes'),
    path('admin_delete_notes/<int:id>/', views.admin_delete_notes, name='admin_delete_notes'),
]