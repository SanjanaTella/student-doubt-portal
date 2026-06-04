from django.contrib import admin
from django.urls import path
from doubts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_doubt/', views.add_doubt, name='add_doubt'),
    path('view_doubts/', views.view_doubts, name='view_doubts'),
    path('edit_doubt/<int:id>/', views.edit_doubt, name='edit_doubt'),
    path('delete_doubt/<int:id>/', views.delete_doubt, name='delete_doubt'),
    path('feedback/', views.feedback, name='feedback'),
]