from django.urls import path
from blogs import views

app_name = "blogs"

urlpatterns = [
    path('', views.PostListView.as_view(), name = 'post_list'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('newpost/', views.CreateNewPost.as_view(), name = 'post_form'),
    path('comment/<int:pk>/', views.CreateNewComment.as_view(), name = 'comment_form'),
    path('postdetail/<int:pk>/', views.PostDetail.as_view(), name = 'post_detail'),
    path('postdelete/<int:pk>/', views.PostDelete.as_view(), name = 'post_delete'),
    path('postpublish/<int:pk>', views.post_publish, name = 'post_publish')
]
