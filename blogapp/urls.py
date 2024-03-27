from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('create_post/', views.create_post, name='create_post'),
    path('contact/', views.contact, name='contact'),
]