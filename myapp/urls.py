from django.urls import path
from . import views

urlpatterns =[
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('profile',views.profile,name='profile'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('blog_write',views.blog_write,name='blog_write'),
    path('blog_update/<str:pk>/',views.blog_update,name='blog_update'),
    path('blog_delete/<str:pk>/',views.blog_delete,name='blog_delete'),
    path('myblog',views.myblog,name='myblog'),
    path('blog',views.blog,name='blog')
]