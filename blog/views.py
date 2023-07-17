from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from .models import Post, Comment
from .forms import PostForm, CommentForm


# Create your views here.
class PostList(View):
    def get(self, request):
        posts = Post.objects.all().order_by('-created_at')
        if request.GET.get('sort'):
            sort = request.GET.get('sort')
            print(request.GET.get('sort'))
        else:
            sort = 'created_at'
        posts = sorted(posts, key=lambda x: getattr(x, sort))
        context = {
            "posts": posts,
        }
        return render(request, "blog/post_list.html", context)


class PostWrite(View):
    def get(self, request):
        form = PostForm
        context = {
            "form": form,
        }
        return render(request, "blog/post_write.html", context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user:
                post.writer = request.user
            post.save()
            return redirect("blog:list")

        return redirect("blog:list")


class PostDetail(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        post.views += 1
        post.save()
        context = {
            "post": post,
            "comment_form": CommentForm,
        }
        print(post_id)
        return render(request, "blog/post_detail.html", context)


class PostEdit(View):
    def get(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = PostForm(instance=post)
        context = {
            "form": form,
            "post": post,
        }
        return render(request, "blog/post_edit.html", context)

    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog:detail", post_id=post_id)
        return redirect("blog:list")


class PostDelete(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        post.delete()
        return redirect("blog:list")


class PostSearch(View):
    def get(self, request):
        query = request.GET.get('q')
        opt = request.GET.get('q-opt')
        print('\n\n\n\n\n\n\n\n\n opt : ', opt)
        print(query)

        # 빈 쿼리 또는 select 에러 시 전체 list
        if not query or opt not in '1234':
            return redirect('blog:list')

        # select에 따른 qeury 결과
        if opt == '1':  # 제목/내용
            result = list(Post.objects.filter(
                Q(content__icontains=query) | Q(title__icontains=query)))
        elif opt == '2':  # 댓글
            comments = list(Comment.objects.filter(content__icontains=query))
            result = [comment.post for comment in comments]
        elif opt == '3':  # 카테고리
            pass
        elif opt == '4':  # 태그
            pass
        else:
            result = None

        # rusult에 따른 context
        if result:
            context = {
                'posts': result
            }
        else:
            context = {
                'posts': None,
                'query': True,
            }
        print('쿼리 : ', query)
        print('결과 : ', result)
        return render(request, "blog/post_list.html", context)


class PostLike(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        post.views -= 1
        post.likes += 1
        post.save()
        return redirect('blog:detail', post_id)


# Comment
class CommentWrite(View):
    def post(self, request, post_id):
        post = Post.objects.get(pk=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.writer = request.user
            comment.save()
            return redirect("blog:detail", post_id=post_id)


class CommentDelete(View):
    def post(self, request, comment_id):
        comment = Comment.objects.get(pk=comment_id)
        post = comment.post
        comment.delete()
        return redirect("blog:detail", post_id=post.pk)
