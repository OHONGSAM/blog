from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostList.as_view(), name="list"),
    path("write/", views.PostWrite.as_view(), name="write"),
    path("detail/<int:post_id>/", views.PostDetail.as_view(), name="detail"),
    path("detail/<int:post_id>/edit/", views.PostEdit.as_view(), name="edit"),
    path("detail/<int:post_id>/delete/",
         views.PostDelete.as_view(), name="delete"),
    path("detail/<int:post_id>/comment/write",
         views.CommentWrite.as_view(), name="cm-write"),
    path("detail/comment/<int:comment_id>/delete",
         views.CommentDelete.as_view(), name="cm-delete"),
    path("search/", views.PostSearch.as_view(), name='search'),
    path("detail/<int:post_id>/like", views.PostLike.as_view(), name='like'),
    path('hot/', views.PostListHot.as_view(), name='hot'),
]
