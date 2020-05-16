from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from instagram.models import Post
from django.urls import reverse_lazy

class signUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

#TemplateView renders html.
class listOfPostsView(ListView):
    model = Post
    template_name = 'index.html'

class postDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class postCreateView(CreateView):
    model = Post
    fields = '__all__'
    template_name = 'new_post.html'

class postEditView(UpdateView):
    model = Post
    fields = '__all__'
    template_name = 'edit_post.html'

class postDeleteView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('postsList')