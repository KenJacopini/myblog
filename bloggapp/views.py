from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date_lte=timezone.now().order_by_('published_date'))
    return render(request, 'bloggapp/post_list.html', {})
