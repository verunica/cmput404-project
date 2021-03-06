from django.conf.urls import url

from . import views

app_name = 'service'


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/(?P<id>[^/]+)/comments/?$', views.posts_comments_handler, name='comment_handler'),
    url(r'^posts/?$', views.posts_handler_generic, name='post_handler_generic'),
    url(r'^posts/(?P<id>[^/]+)/?$', views.posts_handler_specific,name='post_handler_specific'),
    url(r'^author/posts/?$', views.author_posts_handler),
    url(r'^author/(?P<id>[^/]+)/?$', views.author_handler, name='author_handler'),
    url(r'^friends/(?P<author1_id>[0-9a-z-]+)/(?P<author2_id>[0-9a-z-]+)/?$', views.friend_query_handler, name='friend_query_handler'),
    url(r'^friends/(?P<id>[^/]+)/?$', views.friend_handler_specific, name='friend_handler_specific'),
    url(r'^friends/?$', views.friend_handler, name='friend_handler'),
    url(r'^friendrequest/?$', views.friendrequest_handler, name='friendrequest_handler'),
    url(r'^me/?$', views.get_me, name='me'), #endpoint for angular
]
