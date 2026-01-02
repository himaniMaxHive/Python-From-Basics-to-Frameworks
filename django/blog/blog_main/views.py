from django.shortcuts import render
from blogs.models import Category, Blog
from assignments.models import About
def home(request):
    # fetch categories from model
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    # fetch about us
    try:
        about=About.objects.get() # get will fetch only 1 data
    except:
        about=None
    context = {
        'featured_posts': featured_posts,
        'posts':posts,
        'about':about}
    return render(request, 'home.html',context)