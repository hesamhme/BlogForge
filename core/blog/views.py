from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category


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