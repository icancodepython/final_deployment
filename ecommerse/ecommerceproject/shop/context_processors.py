from .models import Category

# To save all the links in a catergory

def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

