from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post


class PostCreateViews(CreateView):
    model = Post
    fields = ['title', 'content', 'status', 'category', 'publish_date']
    success_url = '/blog/post/'
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = '/blog/post/'


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/post/'