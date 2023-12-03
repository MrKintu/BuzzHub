from django.urls import path
from post.views import index, NewPost, PostDetail, Tags, like, favourite

urlpatterns = [
    path('', index, name='index'),
    path('new-post', NewPost, name='new-post'),
    path('<uuid:post_id>', PostDetail, name='post-details'),
    path('tag/<slug:tag_slug>', Tags, name='tags'),
    path('<uuid:post_id>/like', like, name='like'),
    path('<uuid:post_id>/favourite', favourite, name='favourite'),

]
