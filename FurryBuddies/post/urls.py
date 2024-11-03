from django.urls import path

from FurryBuddies.post.views import index, dashboard, create_post, post_details, edit_post, delete_post

urlpatterns = [
    path('', index, name='index'),
    path('posts/dashboard/', dashboard, name='dashboard'),
    path('posts/create/', create_post, name='create-post'),
    path('posts/<int:pk>/details', post_details, name='post-details'),
    path('posts/<int:pk>/edit', edit_post, name='edit-post'),
    path('posts/<int:pk>/delete', delete_post, name='delete-post')
]