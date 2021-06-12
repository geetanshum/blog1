from django.shortcuts import get_object_or_404, render
from .models import blog

# Create your views here.


def allblogs(request):
    blogs = blog.objects.all()
    return render(request, 'allblogs.html', {'blogs': blogs})


def details(request, blog_id):
    blogdetails = get_object_or_404(blog, pk=blog_id)
    return render(request, 'details.html', {'blog': blogdetails})
