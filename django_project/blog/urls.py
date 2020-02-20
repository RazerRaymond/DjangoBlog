from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('createNewPost/',views.create,name='blog-create'),
    path('blog/<int:pk>/',views.blog_detail,name="blog-detail"),
    path('blog/<category>/',views.category,name="blog-category"),
    path('delete/<int:pk>/',views.delete,name="blog-delete"),
    path('edit/<int:pk>/',views.edit,name="blog-edit"),
    path('archive/<int:pk>',views.archive,name="blog-archive"),
    path('archive/',views.archived,name="blog-archived"),
    path('unarchive/<int:pk>',views.unarchive,name="blog-unarchive"),
    path('like/<int:pk>/',views.like,name="blog-like"),
    path('dislike/<int:pk>/',views.dislike,name="blog-dislike")
]