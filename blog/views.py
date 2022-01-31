from .models import Post
from django.views.generic import ListView, DetailView

class PostList(ListView):
    model = Post
#   역순 처리 '-**'
    ordering = '-pk'

# indes(request)관습적으로 리퀘스트 함.
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
