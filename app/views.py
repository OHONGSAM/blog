from django.shortcuts import render, redirect
from django.views import View
from blog.models import Post


class IndexMain(View):
    def get(self, request):
        hotposts = Post.objects.order_by("-likes")[:5]
        if hotposts:
            for post in hotposts:
                post.content = post.content[:30] + "…"
            toppost = hotposts[0]
            context = {
                "top": toppost,
                "posts": hotposts[1:],
            }
        else:
            context = {
                "top": None,
                "posts": None,
            }

        return render(request, "index.html", context)
