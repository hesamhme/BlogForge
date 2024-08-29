from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category


class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    