from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from instagram.views import signUpView, listOfPostsView, postDetailView, postCreateView, postEditView, postDeleteView

urlpatterns = [
    # We have mapped insta/ to Insta.urls in project-level url file so that entering insta/ enables us to jump in Insta.urls.
    path('', listOfPostsView.as_view(), name = 'postsList'),
    path('signup/', signUpView.as_view(), name = 'sign_up'),
    path('posts/<int:pk>/', postDetailView.as_view(), name='post_detail'),
    path('posts/new/', postCreateView.as_view(), name='new_post'),
    path('posts/edit/<int:pk>', postEditView.as_view(), name='edit_post'),
    path('posts/delete/<int:pk>', postDeleteView.as_view(), name='delete_post')
]