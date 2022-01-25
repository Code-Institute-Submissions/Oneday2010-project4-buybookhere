from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Blog

# Create your views here.

def blog(request):
    """ A view to display all blogs """
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """A view to show individual blog post"""
    blog = get_object_or_404(Blog, pk=blog_id)

    context = {
        'blog': blog,
        }

    return render(request, 'blog/blog_detail.html', context)