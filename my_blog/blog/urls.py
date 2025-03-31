from django.urls import path

from . import views

urlpatterns = [
    path("", views.starting_page, name="starting_page"),
    path("posts", views.posts, name="posts_complete_page"),
    # /posts/my-first-post called as a unique identifier are slug
    path("posts/<slug>", views.blog_post_complete_detail, name="post_details_page")
]
