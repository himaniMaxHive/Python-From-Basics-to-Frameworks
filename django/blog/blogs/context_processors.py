from .models import Category

def get_catogries(request):
    categories = Category.objects.all()
    return dict(categories=categories)