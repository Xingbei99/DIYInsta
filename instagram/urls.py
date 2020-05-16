from django.urls import path

from Insta.views import HelloDjango, PostsView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, SignUp

urlpatterns = [
    # We have mapped insta/ to Insta.urls in project-level url file so that entering insta/ enables us to jump in Insta.urls.
    path('posts/', PostsView.as_view(), name='posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='make_post'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='update_post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete_post'),
    path('auth/signup', SignUp.as_view(), name='signup'),
]