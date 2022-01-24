from .models import Post
from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post
    ordering = '-pk'
# def index(request):
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts,
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post' : post
#         }
#     )

class PostDetail(DetailView):
    model = Post
