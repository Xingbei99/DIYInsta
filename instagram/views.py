from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from instagram.models import Post

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