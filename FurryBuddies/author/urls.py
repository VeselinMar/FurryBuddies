from django.urls import path

from FurryBuddies.author.views import create_author_profile, AuthorDetailView, AuthorEditView, AuthorDeleteView

urlpatterns = [
    path('create/', create_author_profile, name='author-create'),
    path('details/', AuthorDetailView.as_view(), name='author-details'),
    path('edit/', AuthorEditView.as_view(), name='author-edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author-delete'),
]