from .models import Category
from assignments.models import SocialLinks

def get_catogries(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_links(request):
    social_links = SocialLinks.objects.all()
    return dict(social_links=social_links)