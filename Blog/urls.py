from django.urls import path
from. import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('contact.html', views.contactPage, name='contact'),
    path('post.html/<str:pk>/', views.postPage, name='post'),
    path('about.html/', views.aboutPage, name='about'),
    path('profile.html', views.userPage, name='profile'),
    path('like/<str:pk>/', views.likePage, name='like'),
    path('edit.html', views.editProfile, name='edit'),
    #path('writer/<str:pk>/', views.writerPage, name='writer'),
]

