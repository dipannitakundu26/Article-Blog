
from django.urls import path
from .views import HomeView,ArticledetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,CategoryView
from .import views
urlpatterns = [
  #path('', views.HomeView, name='home'),
  path('', HomeView.as_view(), name='homeview'),
  path('article/<int:pk>', ArticledetailView.as_view(), name='article-detail'),
  path('addpost/', AddPostView.as_view(), name='addpost'),
  path('article/edit/<int:pk>', UpdatePostView.as_view(), name='editpost'),
  path('article/<int:pk>/delete', DeletePostView.as_view(), name='deletepost'),
  path('category/<str:cats>/', CategoryView, name='category'),
  path('addcategory/', AddCategoryView.as_view(), name='addcategory'),
]