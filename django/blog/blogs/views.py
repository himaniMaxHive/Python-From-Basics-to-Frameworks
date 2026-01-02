from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Category, Blog
from django.db.models import Q
# Create your views here.

def post_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(status = 'Published', category = category_id)
    # if category does not exit, and you want to redirect user somewhere
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')

    # use get_object_or_404 when you want to show 4040 error page
    category = get_object_or_404(Category, pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request,'post_by_category.html',context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'single_blog': single_blog
    }
    return render(request, 'blogs.html', context)

def search(request):
    keyword = request.GET.get("keyword") # here, keyword of input box name attribute
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    print("Blogs: ",blogs)
    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request, 'search.html',context)