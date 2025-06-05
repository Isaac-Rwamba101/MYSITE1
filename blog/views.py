from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404


# Create your views here.
def post_detail(request, year,month, day, post):
        post = get_object_or_404(
              Post,
              status=Post.Status.PUBLISHED,
              slug=post,
                publish__year=year,
                publish__month=month,
                publish__day=day   # Example year, adjust as needed
        )
        return render(
            request,
            'blog/post/detail.html',
            {'post': post}
        )
        
def post_list(request):
    post_list = Post.published.all()
    # Show 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page',1)
    posts = paginator.get_page(page_number)  
    context = {'posts': posts}

    return render(request, 'blog/post/list.html', context)